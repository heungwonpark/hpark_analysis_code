#!/fh/fast/subramaniam_a/user/rasi/virtualenv/default2/bin/python
# -*- coding: utf-8 -*-

'''Calculate summary statistics for each sample.
'''
import numpy as np
import pandas as pd
from commonfunctions import readdata

# datapoints below this threshold are ignored for summary statistics
thresholds = {
    'fitc_a': 0,
    'fsc_a': 0,
    'ssc_a': 0,
}

datadict = readdata()
# concatenate all dataframes
data = pd.concat(datadict, axis=1)
data.columns.names = ['sample', 'channel']
# calculate summary statistics
statistics = {
    'mean': np.mean,
    'median': np.median}

summary = dict()

for col in data:
    if col[1] not in ['fsc_a', 'ssc_a', 'fitc_a', 'pe_texas_red_a']:
        continue
    if col[1] not in summary:
        summary[col[1]] = dict()
    for statistic, func in statistics.items():
        if statistic not in summary[col[1]]:
            summary[col[1]][statistic] = dict()
        if col[1] in thresholds:
            subset = data[col] > thresholds[col[1]]
        else:
            subset = data.index
        summary[col[1]][statistic][col[0]] = func(data[col].ix[subset])
for channel in summary:
    summary[channel] = pd.DataFrame.from_dict(summary[channel])
summarydf = pd.concat(summary, axis=1).astype(int)
summarydf.to_csv('../tables/sumarystatistics.tsv', sep='\t')
