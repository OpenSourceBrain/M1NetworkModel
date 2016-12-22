"""
params.py 

cfg is an object containing a set of simulation configurations using a standardized structure

Contributors: salvadordura@gmail.com
"""

from netpyne import specs

cfg = specs.SimConfig()   # object of class SimConfig to store the simulation configuration

###############################################################################
# SIMULATION CONFIGURATION
###############################################################################

# Simulation parameters
cfg.duration = 0.3*1e3 # Duration of the simulation, in ms
cfg.dt = 0.05 # Internal integration timestep to use
cfg.seeds = {'conn': 1, 'stim': 1, 'loc': 1} # Seeds for randomizers (connectivity, input stimulation and cell locations)
cfg.createNEURONObj = 1  # create HOC objects when instantiating network
cfg.createPyStruct = 1  # create Python structure (simulator-independent) when instantiating network
cfg.verbose = 0 # Whether to write diagnostic information on events 
cfg.hParams = {'celsius': 34, 'v_init': -65}  # set celsius temp

# Recording 
cfg.recordCells = [('PT_L5B',0), ('IT_L5A',0), ('IT_L5B',0)]  # list of cells to record from (those selected for plotting below, will be recorded automatically)
cfg.recordTraces = {'V_soma':{'sec': 'soma', 'loc': 0.5, 'var': 'v'}}

cfg.recordStims = False  # record spikes of cell stims
cfg.recordStep = 0.1 # Step size in ms to save data (eg. V traces, LFP, etc)

# Saving
cfg.simLabel = 'M1_cell'
cfg.saveFolder = '../data/'
cfg.savePickle = False # save to pickle file
cfg.saveJson = True # save to json file
cfg.saveMat = False # save to mat file
cfg.saveDataInclude = ['simData', 'simConfig', 'netParams']
cfg.gatherOnlySimData = False

# Analysis and plotting 
#cfg.addAnalysis('plotRaster', True) # Whether or not to plot a raster
cfg.addAnalysis('plotTraces', {'include': [0], 'saveFig': True, 'showFig': False}) # plot recorded traces for this list of cells

# batch parameters
cfg.sec = 'soma'
cfg.loc = 0.5
cfg.weight = 0.0004



