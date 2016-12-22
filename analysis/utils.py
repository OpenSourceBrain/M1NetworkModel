"""
utils.py 

General functions to analyse simulation data

Contributors: salvadordura@gmail.com
"""
import json
import numpy as np
from pylab import *
from itertools import product
from netpyne import specs

def readBatchData(dataFolder, batchLabel, load = False, save=True, vars=None, maxCombs=None, listCombs=None):
    # load from previously saved file with all data
    if load:
        print '\nLoading single file with all data...'
        filename = '%s/%s/%s_allData.json' % (dataFolder, batchLabel, batchLabel)
        with open(filename, 'r') as fileObj:
            dataLoad = json.load(fileObj, object_pairs_hook=specs.OrderedDict)
        params = dataLoad['params']
        data = dataLoad['data']
        return params, data

    if isinstance(listCombs, basestring):
        filename = str(listCombs)
        with open(filename, 'r') as fileObj:
            dataLoad = json.load(fileObj)
        listCombs = dataLoad['paramsMatch']

    # read the batch file and cfg
    batchFile = '%s/%s/%s_batch.json' % (dataFolder, batchLabel, batchLabel)
    with open(batchFile, 'r') as fileObj:
        b = json.load(fileObj)['batch']

    # read params labels and ranges
    params = b['params']

    # read vars from all files - store in dict 
    if b['method'] == 'grid':
        labelList, valuesList = zip(*[(p['label'], p['values']) for p in params])
        valueCombinations = product(*(valuesList))
        indexCombinations = product(*[range(len(x)) for x in valuesList])
        data = {}
        print 'Reading data...'
        missing = 0
        for i,(iComb, pComb) in enumerate(zip(indexCombinations, valueCombinations)):
            if (not maxCombs or i<= maxCombs) and (not listCombs or list(pComb) in listCombs):
                print i, iComb
                # read output file
                iCombStr = ''.join([''.join('_'+str(i)) for i in iComb])
                simLabel = b['batchLabel']+iCombStr
                outFile = b['saveFolder']+'/'+simLabel+'.json'
                try:
                    with open(outFile, 'r') as fileObj:
                        output = json.load(fileObj, object_pairs_hook=specs.OrderedDict)

                    # save output file in data dict
                    data[iCombStr] = {}  
                    data[iCombStr]['paramValues'] = pComb  # store param values
                    if not vars: vars = output.keys()
                    for key in vars:
                        data[iCombStr][key] = output[key]

                except:
                    missing = missing + 1
                    output = {}
            else:
                missing = missing + 1

        print '%d files missing' % (missing)

        # save
        if save:
            print 'Saving to single file with all data'
            filename = '%s/%s/%s_allData.json' % (dataFolder, batchLabel, batchLabel)
            dataSave = {'params': params, 'data': data}
            with open(filename, 'w') as fileObj:
                json.dump(dataSave, fileObj)
        
        return params, data
