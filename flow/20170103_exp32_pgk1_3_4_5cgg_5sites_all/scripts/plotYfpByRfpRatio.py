#!/fh/fast/subramaniam_a/user/rasi/virtualenv/default2/bin/python
# -*- coding: utf-8 -*-

'''Plot ratio of YFP to RFP for samples that have RFP in them
'''

from statsmodels.formula.api import ols  # ordinary least squares
from commonfunctions import readdata
import pandas as pd
from scipy.stats import tsem
import re
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from clean_matplotlib_axis import clean_axis
from customize_matplotlib import customize_plots
customize_plots(mpl)

# cells with values below these are excluded from analysis
thresholds = {
    'fitc_a': 800,
    'pe_texas_red_a': 1,
}

data = readdata()
stats = dict()
for key in sorted(data):
    if key.startswith('by4741'):  # these samples do not have mkate2
        continue
    stats[key] = dict()
    subset = data[key][
        (data[key]['fitc_a'] > thresholds['fitc_a']) &
        (data[key]['pe_texas_red_a'] > thresholds['pe_texas_red_a'])]
    # fit least squares
    fit = ols(formula='fitc_a ~ pe_texas_red_a', data=subset)
    stats[key]['yfprfpratio'] = fit.fit().params['pe_texas_red_a']

stats = pd.DataFrame.from_dict(stats, orient='index')

# groupby replicates and calculate mean and sem
rep = stats.groupby(lambda x: re.search('(\w+)_\d+$', x).groups()[0])
avgstats = rep.agg({np.mean, tsem})['yfprfpratio']
newindex = sorted(avgstats.index, key=lambda x: x[-3:])
avgstats = avgstats.ix[newindex]

# plot mean and sem of yfp/mkate2
fig = plt.figure()
axcount = 0
axcount += 1
ydata = avgstats['mean']
bkgd_sample = 'mkate2'
bkgd = avgstats.ix[bkgd_sample]['mean']
ydata = ydata - bkgd
yerr = avgstats['tsem']
xdata = range(len(ydata))
ax = fig.add_subplot(1, 1, axcount)
ax.bar(xdata, ydata, align='center')
ax.errorbar(
    xdata, ydata, yerr, linestyle='None', color='k', marker='None')
clean_axis(['left'])
ax.xaxis.set(ticks=range(len(xdata)))
ax.set(
    xlim=(-0.5, len(xdata) - 0.5),
    ylim=(0, 1.3),
    ylabel='YFP / mKate2')
for (x, y) in zip(xdata, ydata):
    ax.text(x, y + 0.05, '%d' % (y * 100), ha='center')
ticklabels = avgstats.index
ax.set_xticklabels(ticklabels, rotation=45, ha='right')
fig.set_size_inches(6, 4)
plt.tight_layout()
fig.savefig('../fig/yfprfpratio.png')
