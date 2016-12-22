"""
batch.py 

Batch simulation for M1 model using NetPyNE

Contributors: salvadordura@gmail.com
"""
from netpyne.batch import Batch

# Create Batch object
b = Batch(netParamsFile='M1_cell.py')

# Add params
b.params.append({'label': 'sec',    'values': ['soma', 'dend_5', 'apic_47']})
b.params.append({'label': 'weight', 'values': [0.0004, 0.001, 0.0015]})


# Setup
b.batchLabel = 'batch1'
b.saveFolder = '../data/'+b.batchLabel
b.method = 'grid'
b.runCfg = {'type': 'mpi', 
			'script': 'init.py', 
			'skip': True}

# run batch
b.run()


