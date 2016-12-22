"""
ITcell.py 

Code to test the reduced IT cell models

Contributors: salvadordura@gmail.com
"""

import utils
import matplotlib.pyplot as plt

def epsp(params, data):
    plt.style.use('ggplot')

    for key, d in data.iteritems():
        vsoma = d['simData']['V_soma']['cell_0']
        epsp = max(vsoma[2000:3000]) - vsoma[1999] # max voltage between 200 to 300 ms - baseline

        print d['paramValues']
        print  epsp

# main code
if __name__ == '__main__':

    dataFolder = '../data/'
    batchLabel = 'batch1'
    loadFromFile = 0
    saveToFile = 1

    filename = dataFolder+'/'+batchLabel+'/'+batchLabel+'_match.json'
    
    params, data = utils.readBatchData(dataFolder, batchLabel, load=loadFromFile, save=saveToFile) 
    epsp(params, data)

