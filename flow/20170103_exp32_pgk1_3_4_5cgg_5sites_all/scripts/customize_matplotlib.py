#!/fh/fast/subramaniam_a/user/rasi/virtualenv/default2/bin/python
# -*- coding: utf-8 -*-

'''Set custom plotting parameters for all matplotlib figs generated
in this project.
'''


def customize_plots(mpl):
    '''Takes handle to matplotlib as input and sets params'''
    mpl.use('Agg')  # this will prevent using x-windows
    mpl.rcParams['axes.labelsize'] = 12
    mpl.rcParams['axes.titlesize'] = 12
    mpl.rcParams['axes.titleweight'] = 'bold'
    mpl.rcParams['figure.subplot.hspace'] = 0.5
    mpl.rcParams['figure.subplot.wspace'] = 0.5
    mpl.rcParams['font.size'] = 10
    mpl.rcParams['font.sans-serif'] = 'Arial'
    mpl.rcParams['xtick.labelsize'] = 10
    mpl.rcParams['ytick.labelsize'] = 10
    mpl.rcParams['legend.fontsize'] = 10
