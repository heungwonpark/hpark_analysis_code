#!/fh/fast/subramaniam_a/user/rasi/virtualenv/default2/bin/python
# -*- coding: utf-8 -*-

'''Plot scatter plot of different channels for subset of samples
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

scatterchannels = {
    'yfp_vs_rfp': {
        'xchannel': 'fitc_a', 'ychannel': 'pe_texas_red_a'}}

data = readdata()
subsetsamples = sorted(data)[startsample:endsample]

fig = plt.figure()
fig.subplots_adjust(wspace=0.7, hspace=0.7)
plotnumber = 0
for key in subsetsamples:
    for scatterchannel in scatterchannels:
        plotnumber += 1
        xchannel = scatterchannels[scatterchannel]['xchannel']
        ychannel = scatterchannels[scatterchannel]['ychannel']
        subset = data[key][(data[key][xchannel] > 1) &
                           (data[key][ychannel] > 1)]
        ax = fig.add_subplot(
            len(subsetsamples)*len(scatterchannels)/4+1,
            4, plotnumber)
        ax.plot(
            np.log10(np.array(subset[xchannel])),
            np.log10(np.array(subset[ychannel])),
            ' .k', markersize=2)
        clean_axis()
        ax.xaxis.set(major_locator=MaxNLocator(6))
        ax.yaxis.set(major_locator=MaxNLocator(6))
        ax.set(
            xlabel='log10 ' + xchannel,
            ylabel='log10 ' + ychannel,
            xlim=[0, 6],
            ylim=[0, 6])
    ax.set_title(key)
fig.set_size_inches([16, plotnumber])
fig.savefig('../fig/scatterplot.png')
