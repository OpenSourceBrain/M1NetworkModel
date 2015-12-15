"""
params file

netParams is a dict containing a set of network parameters using a standardized structure

simConfig is a dict containing a set of simulation configurations using a standardized structure

Contributors: salvadordura@gmail.com
"""

netParams = {}  # dictionary to store sets of network parameters
simConfig = {}  # dictionary to store sets of simulation configurations


###############################################################################
#
# MPI HH TUTORIAL PARAMS
#
###############################################################################

###############################################################################
# NETWORK PARAMETERS
###############################################################################

# Cell properties list
netParams['cellProps'] = []

## PYR cell properties
cellProp = {'label': 'PYR', 'conditions': {'cellType': 'PYR'},  'sections': {}}

soma = {'geom': {}, 'topol': {}, 'mechs': {}, 'syns': {}, 'Izhi2007Type': 'RS'}  # soma properties
soma['geom'] = {'diam': 18.8, 'L': 18.8, 'Ra': 123.0, 'pt3d': []}
soma['mechs']['hh'] = {'gnabar': 0.12, 'gkbar': 0.036, 'gl': 0.003, 'el': -70} 
soma['syns']['NMDA'] = {'type': 'ExpSyn', 'loc': 0.5, 'tau': 0.1, 'e': 0}

cellProp['sections'] = {'soma': soma}  # add sections to dict
netParams['cellProps'].append(cellProp)  # add dict to list of cell properties


# Population parameters
netParams['popParams'] = []  # create list of populations - each item will contain dict with pop params
netParams['popParams'].append({'popLabel': 'PYR', 'cellModel': 'HH', 'cellType': 'PYR', 'numCells': 500}) # add dict with params for this pop 
netParams['popParams'].append({'popLabel': 'background', 'cellModel': 'NetStim', 'rate': 50, 'noise': 0.5, 'source': 'random'})  # background inputs

netParams['popTagsCopiedToCells'] = ['popLabel', 'cellModel', 'cellType']


# Connectivity parameters
netParams['connParams'] = []  

netParams['connParams'].append(
    {'preTags': {'popLabel': 'PYR'}, 'postTags': {'popLabel': 'PYR'},
    'connFunc': 'randConn', # connection function
    'weight': 0.004,        # weight of each connection
    'delayMean': 13.0,      # mean of delays
    'delayVar': 1.4,        # variance of delays 
    'delayMin': 0.2,        # minimum delays
    'threshold': 10,
    'maxConns': 20})       # threshold

netParams['connParams'].append(
    {'preTags': {'popLabel': 'background'}, 'postTags': {'cellType': 'PYR'}, # background -> PYR
    'connFunc': 'fullConn',
    'weight': 0.1, 
    'syn': 'NMDA',
    'delay': 5})  


###############################################################################
# SIMULATION PARAMETERS
###############################################################################

simConfig = {}  # dictionary to store simConfig

# Simulation parameters
simConfig['duration'] = simConfig['tstop'] = 1*1e3 # Duration of the simulation, in ms
simConfig['dt'] = 0.025 # Internal integration timestep to use
simConfig['randseed'] = 1 # Random seed to use
simConfig['createNEURONObj'] = 1  # create HOC objects when instantiating network
simConfig['createPyStruct'] = 1  # create Python structure (simulator-independent) when instantiating network
simConfig['verbose'] = 1  # show detailed messages 


# Recording 
simConfig['recordTraces'] = True  # whether to record cell traces or not
simConfig['recdict'] = {'Vsoma':{'sec':'soma','pos':0.5,'var':'v'}}
simConfig['simDataVecs'] = ['spkt', 'spkid','stims']+simConfig['recdict'].keys()
simConfig['recordStim'] = True  # record spikes of cell stims
simConfig['recordStep'] = 10 # Step size in ms to save data (eg. V traces, LFP, etc)

# Saving
simConfig['filename'] = '../data/mpiHHTut'  # Set file output name
simConfig['saveFileStep'] = 1000 # step size in ms to save data to disk
simConfig['savePickle'] = True # Whether or not to write spikes etc. to a .mat file
simConfig['saveJson'] = False # Whether or not to write spikes etc. to a .mat file
simConfig['saveJsonSampled'] = False # Whether or not to write subsampled spikes etc. to a .mat file
simConfig['saveMat'] = False # Whether or not to write spikes etc. to a .mat file
simConfig['saveTxt'] = False # save spikes and conn to txt file
simConfig['saveDpk'] = False # save to a .dpk pickled file


# Analysis and plotting 
simConfig['plotRaster'] = True # Whether or not to plot a raster
simConfig['plotPsd'] = False # plot power spectral density
simConfig['maxspikestoplot'] = 3e8 # Maximum number of spikes to plot
simConfig['plotConn'] = False # whether to plot conn matrix
simConfig['plotWeightChanges'] = False # whether to plot weight changes (shown in conn matrix)
simConfig['plot3darch'] = False # plot 3d architecture


