#!/fh/fast/subramaniam_a/user/rasi/virtualenv/default2/bin/python
# -*- coding: utf-8 -*-


def readdata():
    '''reads all data .csv files and returns as a dict of dataframes
    '''
    import pandas as pd
    sampleannotations = pd.read_table(
        '../rawdata/sampleannotations.csv', sep=',', index_col=0)
    data = dict()
    for filename in sampleannotations.index:
        key = sampleannotations.ix[filename]['samplename'].lower()
        data[key] = pd.read_csv(
            '../rawdata/' + filename.replace('.fcs', '.csv'),
            index_col=0)
        # replace all hyphens and spaces by underscores
        data[key].columns = map(
            lambda x: x.replace('-', '_').replace(' ', '_').lower(),
            data[key].columns)
    return data

