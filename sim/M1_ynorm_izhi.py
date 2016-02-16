"""
params.py 

netParams is a dict containing a set of network parameters using a standardized structure

simConfig is a dict containing a set of simulation configurations using a standardized structure

Contributors: salvadordura@gmail.com
"""

from netpyne.params.utils import importCell

netParams = {}  # dictionary to store sets of network parameters
simConfig = {}  # dictionary to store sets of simulation configurations

###############################################################################
#
# M1 6-LAYER ynorm-BASED MODEL
#
###############################################################################

###############################################################################
# NETWORK PARAMETERS
###############################################################################


# General network parameters
netParams['scale'] = 1 # Scale factor for number of cells
netParams['sizeX'] = 300 # x-dimension (horizontal length) size in um
netParams['sizeY'] = 1350 # y-dimension (vertical height or cortical depth) size in um
netParams['sizeZ'] = 300 # z-dimension (horizontal depth) size in um

## General connectivity parameters
netParams['scaleConnWeight'] = 0.00005 # Connection weight scale factor
netParams['defaultDelay'] = 2.0 # default conn delay (ms)
netParams['propVelocity'] = 100.0 # propagation velocity (um/ms)
netParams['probLambda'] = 100.0  # length constant (lambda) for connection probability decay

# Cell properties list
netParams['cellParams'] = []

## IT cell params
cellProp = {'label': 'IT', 'conditions': {'cell_type': 'IT'}, 'sections': {}}
cellProp['sections'] = importCell(fileName='cells/izhi2007.py', cellName='IzhiCell', cellArgs={'type':'RS'})
cellProp['sections']['soma']['syns']['AMPA'] = {'_type': 'MyExp2SynBB', '_loc': 0.5, 'tau1': 0.05, 'tau2':5.3, 'e': 0}  # AMPA
cellProp['sections']['soma']['syns']['NMDA'] = {'_type': 'MyExp2SynNMDABB', '_loc': 0.5, 'tau1NMDA': 15, 'tau2NMDA': 150, 'r': 1, 'e': 0}  # NMDA
cellProp['sections']['soma']['syns']['GABAA'] = {'_type': 'MyExp2SynBB', '_loc': 0.5, 'tau1': 0.07, 'tau2': 9.1, 'e': -80}  # GABAA (fast)
cellProp['sections']['soma']['syns']['GABAB'] = {'_type': 'MyExp2SynBB', '_loc': 0.5, 'tau1': 0.2, 'tau2': 20, 'e': -80}  # GABAB (slow)
netParams['cellParams'].append(cellProp)  # add dict to list of cell properties

## PT cell params
cellProp = {'label': 'PT', 'conditions': {'cell_type': 'PT'}, 'sections': {}}
cellProp['sections'] = importCell(
    fileName='cells/izhi2007.py', cellName='IzhiCell',  cellArgs={'type':'IB'})
cellProp['sections']['soma']['syns']['AMPA'] = {'_type': 'MyExp2SynBB', '_loc': 0.5, 'tau1': 0.05, 'tau2':5.3, 'e': 0}  # AMPA
cellProp['sections']['soma']['syns']['NMDA'] = {'_type': 'MyExp2SynNMDABB', '_loc': 0.5, 'tau1NMDA': 15, 'tau2NMDA': 150, 'r': 1, 'e': 0}  # NMDA
cellProp['sections']['soma']['syns']['GABAA'] = {'_type': 'MyExp2SynBB', '_loc': 0.5, 'tau1': 0.07, 'tau2': 9.1, 'e': -80}  # GABAA (fast)
cellProp['sections']['soma']['syns']['GABAB'] = {'_type': 'MyExp2SynBB', '_loc': 0.5, 'tau1': 0.2, 'tau2': 20, 'e': -80}  # GABAB (slow)
netParams['cellParams'].append(cellProp)  # add dict to list of cell properties

## CT cell params
cellProp = {'label': 'CT', 'conditions': {'cell_type': 'CT'}, 'sections': {}}
cellProp['sections'] = importCell(fileName='cells/izhi2007.py', cellName='IzhiCell', cellArgs={'type':'RS'})
cellProp['sections']['soma']['syns']['AMPA'] = {'_type': 'MyExp2SynBB', '_loc': 0.5, 'tau1': 0.05, 'tau2':5.3, 'e': 0}  # AMPA
cellProp['sections']['soma']['syns']['NMDA'] = {'_type': 'MyExp2SynNMDABB', '_loc': 0.5, 'tau1NMDA': 15, 'tau2NMDA': 150, 'r': 1, 'e': 0}  # NMDA
cellProp['sections']['soma']['syns']['GABAA'] = {'_type': 'MyExp2SynBB', '_loc': 0.5, 'tau1': 0.07, 'tau2': 9.1, 'e': -80}  # GABAA (fast)
cellProp['sections']['soma']['syns']['GABAB'] = {'_type': 'MyExp2SynBB', '_loc': 0.5, 'tau1': 0.2, 'tau2': 20, 'e': -80}  # GABAB (slow)
netParams['cellParams'].append(cellProp)  # add dict to list of cell properties

## SOM cell params
cellProp = {'label': 'SOM', 'conditions': {'cell_type': 'SOM'}, 'sections': {}}
cellProp['sections'] = importCell(fileName='cells/izhi2007.py', cellName='IzhiCell', cellArgs={'type':'LTS'})
cellProp['sections']['soma']['syns']['AMPA'] = {'_type': 'MyExp2SynBB', '_loc': 0.5, 'tau1': 0.05, 'tau2':5.3, 'e': 0}  # AMPA
cellProp['sections']['soma']['syns']['NMDA'] = {'_type': 'MyExp2SynNMDABB', '_loc': 0.5, 'tau1NMDA': 15, 'tau2NMDA': 150, 'r': 1, 'e': 0}  # NMDA
cellProp['sections']['soma']['syns']['GABAA'] = {'_type': 'MyExp2SynBB', '_loc': 0.5, 'tau1': 0.07, 'tau2': 9.1, 'e': -80}  # GABAA (fast)
cellProp['sections']['soma']['syns']['GABAB'] = {'_type': 'MyExp2SynBB', '_loc': 0.5, 'tau1': 0.2, 'tau2': 20, 'e': -80}  # GABAB (slow)
netParams['cellParams'].append(cellProp)  # add dict to list of cell properties 

## PV cell params
cellProp = {'label': 'PV', 'conditions': {'cell_type': 'PV'}, 'sections': {}}
cellProp['sections'] = importCell(fileName='cells/izhi2007.py', cellName='IzhiCell', cellArgs={'type':'FS'})
cellProp['sections']['soma']['syns']['AMPA'] = {'_type': 'MyExp2SynBB', '_loc': 0.5, 'tau1': 0.05, 'tau2':5.3, 'e': 0}  # AMPA
cellProp['sections']['soma']['syns']['NMDA'] = {'_type': 'MyExp2SynNMDABB', '_loc': 0.5, 'tau1NMDA': 15, 'tau2NMDA': 150, 'r': 1, 'e': 0}  # NMDA
cellProp['sections']['soma']['syns']['GABAA'] = {'_type': 'MyExp2SynBB', '_loc': 0.5, 'tau1': 0.07, 'tau2': 9.1, 'e': -80}  # GABAA (fast)
cellProp['sections']['soma']['syns']['GABAB'] = {'_type': 'MyExp2SynBB', '_loc': 0.5, 'tau1': 0.2, 'tau2': 20, 'e': -80}  # GABAB (slow)
netParams['cellParams'].append(cellProp)  # add dict to list of cell properties


## create list of populations, where each item contains a dict with the pop params
netParams['popParams'] = []  
     
netParams['popParams'].append({'popLabel': 'IT_L23', 'cellModel': 'Izhi2007b', 'cell_type': 'IT',  'projTarget': '', 'ynormRange': [0.12, 0.31], 'density': 80e3}) #  L2/3 IT
netParams['popParams'].append({'popLabel': 'IT_L4',  'cellModel': 'Izhi2007b', 'cell_type': 'IT',  'projTarget': '', 'ynormRange': [0.31, 0.41], 'density': 80e3}) #  L4 IT
netParams['popParams'].append({'popLabel': 'IT_L5A', 'cellModel': 'Izhi2007b', 'cell_type': 'IT',  'projTarget': '', 'ynormRange': [0.41, 0.52], 'density': 80e3}) #  L5A IT
netParams['popParams'].append({'popLabel': 'IT_L5B', 'cellModel': 'Izhi2007b', 'cell_type': 'IT',  'projTarget': '', 'ynormRange': [0.52, 0.77], 'density': 40e3}) #  L5B IT
netParams['popParams'].append({'popLabel': 'PT_L5B', 'cellModel': 'Izhi2007b', 'cell_type': 'PT',  'projTarget': '', 'ynormRange': [0.52, 0.77], 'density': 40e3}) #  L5B PT
netParams['popParams'].append({'popLabel': 'IT_L6',  'cellModel': 'Izhi2007b', 'cell_type': 'IT',  'projTarget': '', 'ynormRange': [0.77, 1.0], 'density': 40e3}) #  L6 IT
netParams['popParams'].append({'popLabel': 'CT_L6',  'cellModel': 'Izhi2007b', 'cell_type': 'CT',  'projTarget': '', 'ynormRange': [0.77, 1.0], 'density': 40e3}) #  L6 CT
netParams['popParams'].append({'popLabel': 'PV_L23', 'cellModel': 'Izhi2007b', 'cell_type': 'PV',  'projTarget': '', 'ynormRange': [0.1, 0.31], 'density': 10e3}) #  L2/3 PV (FS)
netParams['popParams'].append({'popLabel': 'SOM_L23','cellModel': 'Izhi2007b', 'cell_type': 'SOM', 'projTarget': '', 'ynormRange': [0.1, 0.31], 'density': 10e3}) #  L2/3 SOM (LTS)
netParams['popParams'].append({'popLabel': 'PV_L5',  'cellModel': 'Izhi2007b', 'cell_type': 'PV',  'projTarget': '', 'ynormRange': [0.31, 0.77], 'density': 10e3}) #  L5 PV (FS)
netParams['popParams'].append({'popLabel': 'SOM_L5', 'cellModel': 'Izhi2007b', 'cell_type': 'SOM', 'projTarget': '', 'ynormRange': [0.31, 0.77], 'density': 10e3}) #  L5 SOM (LTS)
netParams['popParams'].append({'popLabel': 'PV_L6',  'cellModel': 'Izhi2007b', 'cell_type': 'PV',  'projTarget': '', 'ynormRange': [0.77, 1.0], 'density': 10e3}) #  L6 PV (FS)
netParams['popParams'].append({'popLabel': 'SOM_L6', 'cellModel': 'Izhi2007b', 'cell_type': 'SOM', 'projTarget': '', 'ynormRange': [0.77, 1.0], 'density': 10e3}) #  L6 SOM (LTS)
netParams['popParams'].append({'popLabel': 'background_E', 'cellModel': 'NetStim', 'rate': 20, 'noise': 0.5, 'source': 'random'})  # background inputs to Exc
netParams['popParams'].append({'popLabel': 'background_I', 'cellModel': 'NetStim', 'rate': 20, 'noise': 0.5, 'source': 'random'})  # background inputs to Inh

netParams['popTagsCopiedToCells'] = ['popLabel', 'cellModel', 'cell_type', 'projTarget']  # tags from population that are copied over to the cells


# List of connectivity rules/params
netParams['connParams'] = []  

netParams['connParams'].append({'preTags': {'popLabel': 'background_E'}, # background -> E IT,CT
'postTags': {'cell_type': ['IT','CT']}, 
'syn': 'NMDA',
'weight': 0.0002,
'delay': 'gauss(10,5)'})  

netParams['connParams'].append({'preTags': {'popLabel': 'background_E'}, # background -> E PT
'postTags': {'cell_type': ['PT']}, 
'syn': 'NMDA',
'weight': 0.00025,
'delay': 'gauss(10,5)'}) 

netParams['connParams'].append({'preTags': {'popLabel': 'background_I'}, # background -> I PV
'postTags': {'cell_type': ['PV']}, 
'syn': 'NMDA',
'weight': 0.0002,
'delay': 'gauss(10,5)'}) 

netParams['connParams'].append({'preTags': {'popLabel': 'background_I'}, # background -> I SOM
'postTags': {'cell_type': ['SOM']}, 
'syn': 'NMDA',
'weight': 0.0001,
'delay': 'gauss(10,5)'}) 


# Generated using importConnFromExcel() function in params/utils.py 
netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.1,0.2]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.1,0.2]},
'syn': 'AMPA',
'probability': 0.09263,
'weight': 0.64,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.1,0.2]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.2,0.3]},
'syn': 'AMPA',
'probability': 0.05354,
'weight': 0.44,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.1,0.2]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.3,0.4]},
'syn': 'AMPA',
'probability': 0.15907,
'weight': 0.31,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.2,0.3]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.1,0.2]},
'syn': 'AMPA',
'probability': 0.02652,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.2,0.3]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.2,0.3]},
'syn': 'AMPA',
'probability': 0.18713,
'weight': 0.78,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.2,0.3]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.3,0.4]},
'syn': 'AMPA',
'probability': 0.05749,
'weight': 0.36,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.3,0.4]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.1,0.2]},
'syn': 'AMPA',
'probability': 0.02757,
'weight': 0.98,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.3,0.4]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.2,0.3]},
'syn': 'AMPA',
'probability': 0.06036,
'weight': 0.58,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.3,0.4]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.3,0.4]},
'syn': 'AMPA',
'probability': 0.24283,
'weight': 0.95,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.3,0.4]},
'postTags': {'cell_type': ['IT','CT'], 'ynorm': [0.8,0.9]},
'syn': 'AMPA',
'probability': 0.00112,
'weight': 2.27,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.4,0.5]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.1,0.2]},
'syn': 'AMPA',
'probability': 0.05249,
'weight': 0.52,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.4,0.5]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.2,0.3]},
'syn': 'AMPA',
'probability': 0.02253,
'weight': 0.67,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.4,0.5]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.3,0.4]},
'syn': 'AMPA',
'probability': 0.02279,
'weight': 0.48,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.4,0.5]},
'postTags': {'cell_type': ['IT','CT'], 'ynorm': [0.8,0.9]},
'syn': 'AMPA',
'probability': 0.02354,
'weight': 0.28,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.4,0.5]},
'postTags': {'cell_type': ['IT','CT'], 'ynorm': [0.9,1.0]},
'syn': 'AMPA',
'probability': 0.0045,
'weight': 0.28,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.5,0.6]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.1,0.2]},
'syn': 'AMPA',
'probability': 0.03723,
'weight': 0.21,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.5,0.6]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.2,0.3]},
'syn': 'AMPA',
'probability': 0.03549,
'weight': 0.26,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.5,0.6]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.3,0.4]},
'syn': 'AMPA',
'probability': 0.04656,
'weight': 0.17,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.5,0.6]},
'postTags': {'cell_type': ['IT','CT'], 'ynorm': [0.8,0.9]},
'syn': 'AMPA',
'probability': 0.01985,
'weight': 0.49,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.5,0.6]},
'postTags': {'cell_type': ['IT','CT'], 'ynorm': [0.9,1.0]},
'syn': 'AMPA',
'probability': 0.0041,
'weight': 0.49,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.6,0.7]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.1,0.2]},
'syn': 'AMPA',
'probability': 0.0023,
'weight': 0.21,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.6,0.7]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.2,0.3]},
'syn': 'AMPA',
'probability': 0.0164,
'weight': 0.26,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.6,0.7]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.3,0.4]},
'syn': 'AMPA',
'probability': 0.01887,
'weight': 0.17,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.6,0.7]},
'postTags': {'cell_type': ['IT','CT'], 'ynorm': [0.8,0.9]},
'syn': 'AMPA',
'probability': 0.02843,
'weight': 0.49,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.6,0.7]},
'postTags': {'cell_type': ['IT','CT'], 'ynorm': [0.9,1.0]},
'syn': 'AMPA',
'probability': 0.00608,
'weight': 0.49,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.7,0.8]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.2,0.3]},
'syn': 'AMPA',
'probability': 0.00248,
'weight': 0.26,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.7,0.8]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.3,0.4]},
'syn': 'AMPA',
'probability': 0.02445,
'weight': 0.17,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.7,0.8]},
'postTags': {'cell_type': ['IT','CT'], 'ynorm': [0.8,0.9]},
'syn': 'AMPA',
'probability': 0.02534,
'weight': 0.49,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.7,0.8]},
'postTags': {'cell_type': ['IT','CT'], 'ynorm': [0.9,1.0]},
'syn': 'AMPA',
'probability': 0.01239,
'weight': 0.49,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.8,0.9]},
'postTags': {'cell_type': ['IT','CT'], 'ynorm': [0.8,0.9]},
'syn': 'AMPA',
'probability': 0.0282,
'weight': 0.53,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.8,0.9]},
'postTags': {'cell_type': ['IT','CT'], 'ynorm': [0.9,1.0]},
'syn': 'AMPA',
'probability': 0.01523,
'weight': 0.53,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.9,1.0]},
'postTags': {'cell_type': ['IT','CT'], 'ynorm': [0.8,0.9]},
'syn': 'AMPA',
'probability': 0.02209,
'weight': 0.53,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','CT'], 'ynorm': [0.9,1.0]},
'postTags': {'cell_type': ['IT','CT'], 'ynorm': [0.9,1.0]},
'syn': 'AMPA',
'probability': 0.0282,
'weight': 0.53,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0,0.0625]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.3125,0.375]},
'syn': 'AMPA',
'probability': 0.01552,
'weight': 0.31,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0,0.0625]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.375,0.4375]},
'syn': 'AMPA',
'probability': 0.00752,
'weight': 0.43,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0,0.0625]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.00313,
'weight': 0.55,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0,0.0625]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.00161,
'weight': 0.55,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0,0.0625]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.00162,
'weight': 0.22,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0,0.0625]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.00566,
'weight': 0.22,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0,0.0625]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.00283,
'weight': 0.22,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.0625,0.125]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.3125,0.375]},
'syn': 'AMPA',
'probability': 0.01825,
'weight': 0.31,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.0625,0.125]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.375,0.4375]},
'syn': 'AMPA',
'probability': 0.02673,
'weight': 0.43,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.0625,0.125]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.01177,
'weight': 0.55,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.0625,0.125]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.00447,
'weight': 0.55,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.0625,0.125]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.01216,
'weight': 0.22,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.0625,0.125]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.01007,
'weight': 0.22,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.0625,0.125]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.00672,
'weight': 0.22,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.125,0.1875]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.3125,0.375]},
'syn': 'AMPA',
'probability': 0.0199,
'weight': 0.31,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.125,0.1875]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.375,0.4375]},
'syn': 'AMPA',
'probability': 0.25242,
'weight': 0.43,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.125,0.1875]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.10856,
'weight': 0.55,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.125,0.1875]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.01429,
'weight': 0.55,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.125,0.1875]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.0429,
'weight': 0.22,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.125,0.1875]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.0403,
'weight': 0.22,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.125,0.1875]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.01982,
'weight': 0.22,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.1875,0.25]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.3125,0.375]},
'syn': 'AMPA',
'probability': 0.02528,
'weight': 0.36,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.1875,0.25]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.375,0.4375]},
'syn': 'AMPA',
'probability': 0.07305,
'weight': 0.645,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.1875,0.25]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.03289,
'weight': 0.93,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.1875,0.25]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.01182,
'weight': 1.01,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.1875,0.25]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.01017,
'weight': 1.01,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.1875,0.25]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.00814,
'weight': 1.01,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.1875,0.25]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.00615,
'weight': 1.01,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.25,0.3125]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.3125,0.375]},
'syn': 'AMPA',
'probability': 0.03508,
'weight': 0.36,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.25,0.3125]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.375,0.4375]},
'syn': 'AMPA',
'probability': 0.02558,
'weight': 0.645,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.25,0.3125]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.0212,
'weight': 0.93,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.25,0.3125]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.01126,
'weight': 1.01,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.25,0.3125]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.01244,
'weight': 1.01,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.25,0.3125]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.01172,
'weight': 1.01,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.25,0.3125]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.00771,
'weight': 1.01,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.3125,0.375]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.3125,0.375]},
'syn': 'AMPA',
'probability': 0.24283,
'weight': 0.95,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.3125,0.375]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.375,0.4375]},
'syn': 'AMPA',
'probability': 0.02792,
'weight': 0.745,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.3125,0.375]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.02731,
'weight': 0.54,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.3125,0.375]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.01384,
'weight': 0.88,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.3125,0.375]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.01409,
'weight': 0.88,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.3125,0.375]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.02068,
'weight': 0.88,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.3125,0.375]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.01678,
'weight': 0.88,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.375,0.4375]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.3125,0.375]},
'syn': 'AMPA',
'probability': 0.01015,
'weight': 0.715,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.375,0.4375]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.375,0.4375]},
'syn': 'AMPA',
'probability': 0.27108,
'weight': 0.6575,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.375,0.4375]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.02483,
'weight': 0.6,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.375,0.4375]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.01865,
'weight': 0.88,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.375,0.4375]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.01966,
'weight': 0.88,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.375,0.4375]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.02269,
'weight': 0.88,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.4375,0.5]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.375,0.4375]},
'syn': 'AMPA',
'probability': 0.0367,
'weight': 0.57,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.4375,0.5]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.19058,
'weight': 0.66,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.4375,0.5]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.01417,
'weight': 0.88,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.4375,0.5]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.01148,
'weight': 0.88,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.4375,0.5]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.00896,
'weight': 0.88,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.4375,0.5]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.01049,
'weight': 0.88,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.5,0.5625]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.3125,0.375]},
'syn': 'AMPA',
'probability': 0.00516,
'weight': 0.17,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.5,0.5625]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.375,0.4375]},
'syn': 'AMPA',
'probability': 0.06083,
'weight': 0.205,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.5,0.5625]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.05276,
'weight': 0.24,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.5,0.5625]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.07207,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.5,0.5625]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.01464,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.5,0.5625]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.02666,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.5,0.5625]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.0189,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.5625,0.625]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.3125,0.375]},
'syn': 'AMPA',
'probability': 0.02669,
'weight': 0.17,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.5625,0.625]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.375,0.4375]},
'syn': 'AMPA',
'probability': 0.05569,
'weight': 0.205,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.5625,0.625]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.04304,
'weight': 0.24,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.5625,0.625]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.01716,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.5625,0.625]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.07207,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.5625,0.625]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.02512,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.5625,0.625]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.03215,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.625,0.6875]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.3125,0.375]},
'syn': 'AMPA',
'probability': 0.012,
'weight': 0.17,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.625,0.6875]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.375,0.4375]},
'syn': 'AMPA',
'probability': 0.05577,
'weight': 0.205,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.625,0.6875]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.04895,
'weight': 0.24,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.625,0.6875]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.02604,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.625,0.6875]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.02285,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.625,0.6875]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.07207,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.625,0.6875]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.03437,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.6875,0.75]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.3125,0.375]},
'syn': 'AMPA',
'probability': 0.01128,
'weight': 0.17,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.6875,0.75]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.375,0.4375]},
'syn': 'AMPA',
'probability': 0.03357,
'weight': 0.205,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.6875,0.75]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.05406,
'weight': 0.24,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.6875,0.75]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.03109,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.6875,0.75]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.02212,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.6875,0.75]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.03198,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.6875,0.75]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.07207,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.75,0.8125]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.3125,0.375]},
'syn': 'AMPA',
'probability': 0.02865,
'weight': 0.085,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.75,0.8125]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.375,0.4375]},
'syn': 'AMPA',
'probability': 0.03087,
'weight': 0.1225,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.75,0.8125]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.02845,
'weight': 0.16,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.75,0.8125]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.02626,
'weight': 0.505,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.75,0.8125]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.03999,
'weight': 0.505,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.75,0.8125]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.03449,
'weight': 0.505,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.75,0.8125]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.03762,
'weight': 0.505,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.75,0.8125]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.75,0.8125]},
'syn': 'AMPA',
'probability': 0.06514,
'weight': 0.5075,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.8125,0.875]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.375,0.4375]},
'syn': 'AMPA',
'probability': 0.10538,
'weight': 0.04,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.8125,0.875]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.05033,
'weight': 0.08,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.8125,0.875]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.0371,
'weight': 0.3,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.8125,0.875]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.04348,
'weight': 0.3,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.8125,0.875]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.07874,
'weight': 0.3,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.8125,0.875]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.02447,
'weight': 0.3,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.875,0.9375]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.375,0.4375]},
'syn': 'AMPA',
'probability': 0.03777,
'weight': 0.04,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.875,0.9375]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.03426,
'weight': 0.08,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.875,0.9375]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.00944,
'weight': 0.3,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.875,0.9375]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.01732,
'weight': 0.3,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.875,0.9375]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.03038,
'weight': 0.3,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.875,0.9375]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.03983,
'weight': 0.3,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.9375,1.0]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.375,0.4375]},
'syn': 'AMPA',
'probability': 0.01306,
'weight': 0.04,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.9375,1.0]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.0208,
'weight': 0.08,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.9375,1.0]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.00606,
'weight': 0.3,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.9375,1.0]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.01059,
'weight': 0.3,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.9375,1.0]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.01826,
'weight': 0.3,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.9375,1.0]},
'postTags': {'cell_type': 'IT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.02623,
'weight': 0.3,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0,0.0625]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 7e-05,
'weight': 0.55,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0,0.0625]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.00152,
'weight': 0.55,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0,0.0625]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.00175,
'weight': 0.22,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0,0.0625]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.00834,
'weight': 0.22,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0,0.0625]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.00121,
'weight': 0.22,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0,0.0625]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.75,0.8125]},
'syn': 'AMPA',
'probability': 0.0151,
'weight': 0.11,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.0625,0.125]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.00834,
'weight': 0.55,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.0625,0.125]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.03265,
'weight': 0.55,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.0625,0.125]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.0344,
'weight': 0.22,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.0625,0.125]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.05135,
'weight': 0.22,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.0625,0.125]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.02531,
'weight': 0.22,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.125,0.1875]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.15193,
'weight': 0.55,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.125,0.1875]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.19617,
'weight': 0.55,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.125,0.1875]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.32257,
'weight': 0.22,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.125,0.1875]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.11603,
'weight': 0.22,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.125,0.1875]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.04989,
'weight': 0.22,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.125,0.1875]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.75,0.8125]},
'syn': 'AMPA',
'probability': 0.03963,
'weight': 0.11,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.1875,0.25]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.11919,
'weight': 0.93,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.1875,0.25]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.12195,
'weight': 1.01,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.1875,0.25]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.06862,
'weight': 1.01,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.1875,0.25]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.01836,
'weight': 1.01,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.1875,0.25]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.01323,
'weight': 1.01,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.25,0.3125]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.06539,
'weight': 0.93,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.25,0.3125]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.06917,
'weight': 1.01,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.25,0.3125]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.03868,
'weight': 1.01,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.25,0.3125]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.00778,
'weight': 1.01,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.25,0.3125]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.00557,
'weight': 1.01,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.25,0.3125]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.75,0.8125]},
'syn': 'AMPA',
'probability': 0.00954,
'weight': 0.505,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.3125,0.375]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.03477,
'weight': 0.54,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.3125,0.375]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.03161,
'weight': 0.88,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.3125,0.375]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.01466,
'weight': 0.88,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.3125,0.375]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.00559,
'weight': 0.88,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.3125,0.375]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.00364,
'weight': 0.88,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.3125,0.375]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.75,0.8125]},
'syn': 'AMPA',
'probability': 0.0032,
'weight': 1.575,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.375,0.4375]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.012,
'weight': 0.6,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.375,0.4375]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.02515,
'weight': 0.88,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.375,0.4375]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.01581,
'weight': 0.88,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.375,0.4375]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.0112,
'weight': 0.88,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.375,0.4375]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.00632,
'weight': 0.88,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.375,0.4375]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.75,0.8125]},
'syn': 'AMPA',
'probability': 0.00845,
'weight': 1.0775,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.4375,0.5]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.19058,
'weight': 0.66,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.4375,0.5]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.01695,
'weight': 0.88,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.4375,0.5]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.02083,
'weight': 0.88,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.4375,0.5]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.01875,
'weight': 0.88,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.4375,0.5]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.01068,
'weight': 0.88,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.4375,0.5]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.75,0.8125]},
'syn': 'AMPA',
'probability': 0.02621,
'weight': 0.58,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.5,0.5625]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.06517,
'weight': 0.24,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.5,0.5625]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.07207,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.5,0.5625]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.02806,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.5,0.5625]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.02714,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.5,0.5625]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.02555,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.5,0.5625]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.75,0.8125]},
'syn': 'AMPA',
'probability': 0.04785,
'weight': 0.6,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.5625,0.625]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.06122,
'weight': 0.24,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.5625,0.625]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.02694,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.5625,0.625]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.07207,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.5625,0.625]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.04268,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.5625,0.625]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.03144,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.5625,0.625]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.75,0.8125]},
'syn': 'AMPA',
'probability': 0.06465,
'weight': 0.6,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.625,0.6875]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.05847,
'weight': 0.24,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.625,0.6875]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.03243,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.625,0.6875]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.02506,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.625,0.6875]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.07207,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.625,0.6875]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.04815,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.625,0.6875]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.75,0.8125]},
'syn': 'AMPA',
'probability': 0.05065,
'weight': 0.6,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.6875,0.75]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.11183,
'weight': 0.24,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.6875,0.75]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.04361,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.6875,0.75]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.03592,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.6875,0.75]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.03573,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.6875,0.75]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.07207,
'weight': 0.71,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.6875,0.75]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.75,0.8125]},
'syn': 'AMPA',
'probability': 0.03327,
'weight': 0.6,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.75,0.8125]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.0287,
'weight': 0.16,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.75,0.8125]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.03114,
'weight': 0.505,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.75,0.8125]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.04704,
'weight': 0.505,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.75,0.8125]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.064,
'weight': 0.505,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.75,0.8125]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.04217,
'weight': 0.505,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.75,0.8125]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.75,0.8125]},
'syn': 'AMPA',
'probability': 0.10083,
'weight': 0.5075,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.8125,0.875]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.0842,
'weight': 0.08,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.8125,0.875]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.02139,
'weight': 0.3,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.8125,0.875]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.04168,
'weight': 0.3,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.8125,0.875]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.0791,
'weight': 0.3,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.8125,0.875]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.05949,
'weight': 0.3,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.8125,0.875]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.75,0.8125]},
'syn': 'AMPA',
'probability': 0.06274,
'weight': 0.415,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.875,0.9375]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.01194,
'weight': 0.08,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.875,0.9375]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.01487,
'weight': 0.3,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.875,0.9375]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.01159,
'weight': 0.3,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.875,0.9375]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.01603,
'weight': 0.3,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.875,0.9375]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.02624,
'weight': 0.3,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.875,0.9375]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.75,0.8125]},
'syn': 'AMPA',
'probability': 0.02597,
'weight': 0.415,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.9375,1.0]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.4375,0.5]},
'syn': 'AMPA',
'probability': 0.03389,
'weight': 0.08,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.9375,1.0]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5,0.5625]},
'syn': 'AMPA',
'probability': 0.00614,
'weight': 0.3,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.9375,1.0]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.5625,0.625]},
'syn': 'AMPA',
'probability': 0.0087,
'weight': 0.3,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.9375,1.0]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.625,0.6875]},
'syn': 'AMPA',
'probability': 0.01269,
'weight': 0.3,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.9375,1.0]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.6875,0.75]},
'syn': 'AMPA',
'probability': 0.0154,
'weight': 0.3,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'cell_type': ['IT','PT','CT'], 'ynorm': [0.9375,1.0]},
'postTags': {'cell_type': 'PT', 'ynorm': [0.75,0.8125]},
'syn': 'AMPA',
'probability': 0.01161,
'weight': 0.415,
'delay': 'defaultDelay+dist_3D/propVelocity'})


netParams['connParams'].append({'preTags': {'popLabel': 'IT_L23'},
'postTags': {'popLabel': 'SOM_L23'},
'syn': 'AMPA',
'probability': 0.18713,
'weight': 0.78,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'popLabel': 'IT_L23'},
'postTags': {'popLabel': 'SOM_L5'},
'syn': 'AMPA',
'probability': 0.21712,
'weight': 1.01,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'popLabel': ['IT_L4','IT_L5A','IT_L5B','PT_L5B']},
'postTags': {'popLabel': 'SOM_L23'},
'syn': 'AMPA',
'probability': 0.02222,
'weight': 0.3625,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'popLabel': ['IT_L4','IT_L5A','IT_L5B','PT_L5B']},
'postTags': {'popLabel': 'SOM_L5'},
'syn': 'AMPA',
'probability': 0.03494,
'weight': 0.1225,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'popLabel': ['IT_L4','IT_L5A','IT_L5B','PT_L5B']},
'postTags': {'popLabel': 'SOM_L6'},
'syn': 'AMPA',
'probability': 0.01553,
'weight': 0.4375,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'popLabel': ['IT_L6','CT_L6']},
'postTags': {'popLabel': 'SOM_L5'},
'syn': 'AMPA',
'probability': 0.02485,
'weight': 0.24786,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'popLabel': ['IT_L6','CT_L6']},
'postTags': {'popLabel': 'SOM_L6'},
'syn': 'AMPA',
'probability': 0.02343,
'weight': 0.53,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'popLabel': 'IT_L23'},
'postTags': {'popLabel': 'PV_L23'},
'syn': 'AMPA',
'probability': 0.18713,
'weight': 0.78,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'popLabel': 'IT_L23'},
'postTags': {'popLabel': 'PV_L5'},
'syn': 'AMPA',
'probability': 0.01996,
'weight': 0.11,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'popLabel': ['IT_L4','IT_L5A','IT_L5B','PT_L5B']},
'postTags': {'popLabel': 'PV_L23'},
'syn': 'AMPA',
'probability': 0.02222,
'weight': 0.3625,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'popLabel': ['IT_L4','IT_L5A','IT_L5B','PT_L5B']},
'postTags': {'popLabel': 'PV_L5'},
'syn': 'AMPA',
'probability': 0.19058,
'weight': 1.0775,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'popLabel': ['IT_L4','IT_L5A','IT_L5B','PT_L5B']},
'postTags': {'popLabel': 'PV_L6'},
'syn': 'AMPA',
'probability': 0.01553,
'weight': 0.4375,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'popLabel': ['IT_L6','CT_L6']},
'postTags': {'popLabel': 'PV_L5'},
'syn': 'AMPA',
'probability': 0.02485,
'weight': 0.24786,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'popLabel': ['IT_L6','CT_L6']},
'postTags': {'popLabel': 'PV_L6'},
'syn': 'AMPA',
'probability': 0.02343,
'weight': 0.53,
'delay': 'defaultDelay+dist_3D/propVelocity'})


netParams['connParams'].append({'preTags': {'popLabel': 'SOM_L23'},
'postTags': {'ynorm': [0.12,0.31]},
'syn': 'GABAB',
'probability': '1.0 * exp(-dist_3D/probLambda)',
'weight': 1.5,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'popLabel': 'SOM_L5'},
'postTags': {'ynorm': [0.31,0.77]},
'syn': 'GABAB',
'probability': '1.0 * exp(-dist_3D/probLambda)',
'weight': 1.5,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'popLabel': 'SOM_L6'},
'postTags': {'ynorm': [0.77,1.0]},
'syn': 'GABAB',
'probability': '1.0 * exp(-dist_3D/probLambda)',
'weight': 1.5,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'popLabel': 'PV_L23'},
'postTags': {'ynorm': [0.12,0.31]},
'syn': 'GABAA',
'probability': '1.0 * exp(-dist_3D/probLambda)',
'weight': 1.5,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'popLabel': 'PV_L5'},
'postTags': {'ynorm': [0.31,0.77]},
'syn': 'GABAA',
'probability': '1.0 * exp(-dist_3D/probLambda)',
'weight': 1.5,
'delay': 'defaultDelay+dist_3D/propVelocity'})

netParams['connParams'].append({'preTags': {'popLabel': 'PV_L6'},
'postTags': {'ynorm': [0.77,1.0]},
'syn': 'GABAA',
'probability': '1.0 * exp(-dist_3D/probLambda)',
'weight': 1.5,
'delay': 'defaultDelay+dist_3D/propVelocity'})
#'''


# Dictionary of annotations
netParams['annots'] = {}


###############################################################################
# SIMULATION CONFIGURATION
###############################################################################

simConfig = {}  # dictionary to store simConfig

# Simulation parameters
simConfig['duration'] = simConfig['tstop'] = 1*1e3 # Duration of the simulation, in ms
simConfig['dt'] = 0.5 # Internal integration timestep to use
simConfig['randseed'] = 1 # Random seed to use
simConfig['createNEURONObj'] = 1  # create HOC objects when instantiating network
simConfig['createPyStruct'] = 1  # create Python structure (simulator-independent) when instantiating network
simConfig['verbose'] = 0 # Whether to write diagnostic information on events 


# Recording 
simConfig['recordTraces'] = True  # whether to record cell traces or not
simConfig['recordDict'] = {} # 'V':{'sec':'soma','pos':0.5,'var':'v'}}
	#'V':{'sec':'soma','pos':0.5,'var':'v'}, 
    #'u':{'sec':'soma', 'pointp':'Izhi2007b_0', 'var':'u'}, 
    #'I':{'sec':'soma', 'pointp':'Izhi2007b_0', 'var':'i'}, 
    #'AMPA_i': {'sec':'soma', 'pos':'0.5', 'syn':'AMPA', 'var':'i'},
    #'NMDA_i': {'sec':'soma', 'pos':'0.5', 'syn':'NMDA', 'var':'iNMDA'}}  # Dict of traces to record
simConfig['simDataVecs'] = ['spkt', 'spkid','stims']+simConfig['recordDict'].keys()
simConfig['recordStim'] = False  # record spikes of cell stims
simConfig['recordStep'] = 0.5 # Step size in ms to save data (eg. V traces, LFP, etc)

# Saving
simConfig['filename'] = '../data/M1_ynorm_izhi_correct'  # Set file output name
simConfig['saveFileStep'] = 1000 # step size in ms to save data to disk
simConfig['savePickle'] = False # save to pickle file
simConfig['saveJson'] = False # save to json file
simConfig['saveMat'] = False # save to mat file
simConfig['saveTxt'] = False # save to txt file
simConfig['saveDpk'] = False # save to .dpk pickled file
simConfig['saveHDF5'] = False # save to HDF5 file 


# Analysis and plotting 
simConfig['plotRaster'] = True # Whether or not to plot a raster
simConfig['orderRasterYnorm'] = 0 # Order cells in raster by yfrac (default is by pop and cell id)
simConfig['plotTracesGids'] = [] # plot recorded traces for this list of cells
simConfig['plotLFPSpectrum'] = False # plot power spectral density (not yet implemented)
simConfig['plotConn'] = False # whether to plot conn matrix (not yet implemented)


