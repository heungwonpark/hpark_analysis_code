#!/fh/fast/subramaniam_a/user/rasi/virtualenv/default2/bin/python
# -*- coding: utf-8 -*-

'''Plot histogram of all channels for subset of samples
'''

import numpy as np
from commonfunctions import readdata
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from clean_matplotlib_axis import clean_axis
from customize_matplotlib import customize_plots
customize_plots(mpl)

# only these subset samples are plotted
# in case there are too many samples
startsample = 10
endsample = 20

data = readdata()
subsetsamples = sorted(data)[startsample:endsample]

fig = plt.figure()
fig.subplots_adjust(wspace=0.7, hspace=0.7)
plotnumber = 0
for key in subsetsamples:
    for channel in ['fsc_a', 'ssc_a', 'fitc_a', 'pe_texas_red_a']:
        plotnumber += 1
        subset = data[key][(data[key][channel] > 1)]
        ax = fig.add_subplot(
            len(subsetsamples), 4, plotnumber)
        ax.hist(np.log10(np.array(subset[channel])), 50)
        clean_axis(['left'])
        ax.yaxis.set(major_locator=MaxNLocator(5))
        ax.set(
            xlabel='log10 ' + channel,
            ylabel='counts',
            xlim=[0, 6])
        if channel == 'ssc_a':
            ax.set_title(key, position=(1.2, 1.2))
fig.set_size_inches([16, 4 * len(subsetsamples)])
fig.savefig('../fig/histogram.png')
