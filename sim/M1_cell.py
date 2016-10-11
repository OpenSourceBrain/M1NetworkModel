"""
params.py 

netParams is an object containing a set of network parameters using a standardized structure

simConfig is an object containing a set of simulation configurations using a standardized structure

Contributors: salvadordura@gmail.com
"""

from netpyne import specs
import pickle

netParams = specs.NetParams()   # object of class NetParams to store the network parameters
simConfig = specs.SimConfig()   # object of class SimConfig to store the simulation configuration

###############################################################################
#
# M1 6-LAYER ynorm-BASED MODEL
#
###############################################################################

###############################################################################
# SIMULATION CONFIGURATION
###############################################################################

# Simulation parameters
simConfig.duration = 0.1*1e3 # Duration of the simulation, in ms
simConfig.dt = 0.01 # Internal integration timestep to use
simConfig.seeds = {'conn': 1, 'stim': 1, 'loc': 1} # Seeds for randomizers (connectivity, input stimulation and cell locations)
simConfig.createNEURONObj = 1  # create HOC objects when instantiating network
simConfig.createPyStruct = 1  # create Python structure (simulator-independent) when instantiating network
simConfig.verbose = 0 # Whether to write diagnostic information on events 
simConfig.hParams = {'celsius': 34, 'v_init': -65}  # set celsius temp

# Recording 
simConfig.recordCells = [('PT_L5B',0)]  # list of cells to record from (those selected for plotting below, will be recorded automatically)
simConfig.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}

# record for 5-comp
# simConfig['recordTraces'] =	{'VAdend1':{'sec':'Adend1','loc':0.5,'var':'v'},
# 							'Vsoma': {'sec':'soma','loc':0.5,'var':'v'}} 

# record for full cell
							#'V_basal':{'sec':'dend_30','loc':0.5,'var':'v'}}
							# 'V_maintrunk':{'sec':'apic_10','loc':0.5,'var':'v'},
							# 'V_oblique':{'sec':'apic_90','loc':0.5,'var':'v'},
							# 'V_uppertrunk':{'sec':'apic_46','loc':0.5,'var':'v'},
							# 'V_tuft':{'sec':'apic_60','loc':0.5,'var':'v'},
							# 'V_axon':{'sec':'axon','loc':0.5,'var':'v'}} 

# record syns
# simConfig['recordTraces'] = {'AMPA_i': {'sec':'soma', 'loc':'0.5', 'synMech':'AMPA', 'var':'i'},
#     						   'NMDA_i': {'sec':'soma', 'loc':'0.5', 'synMech':'NMDA', 'var':'iNMDA'}}  # Dict of traces to record


simConfig.recordStims = False  # record spikes of cell stims
simConfig.recordStep = 0.1 # Step size in ms to save data (eg. V traces, LFP, etc)

# Saving
simConfig.filename = '../data/M1_cell'  # Set file output name
simConfig.savePickle = False # save to pickle file
simConfig.saveJson = False # save to json file
simConfig.saveMat = False # save to mat file
simConfig.gatherOnlySimData = True

# Analysis and plotting 
simConfig.addAnalysis('plotRaster', True) # Whether or not to plot a raster
simConfig.addAnalysis('plotTraces', {'include': [('PT_L5B',0)]}) # plot recorded traces for this list of cells
#simConfig.addAnalysis('plotConn', True)

###############################################################################
# NETWORK PARAMETERS
###############################################################################

# General network parameters
netParams.scale = 1 # Scale factor for number of cells
netParams.sizeX = 30 # x-dimension (horizontal length) size in um
netParams.sizeY = 1350 # y-dimension (vertical height or cortical depth) size in um
netParams.sizeZ = 30 # z-dimension (horizontal depth) size in um

## General connectivity parameters
netParams.scaleConnWeight = 1.0 # Connection weight scale factor (default if no model specified)
netParams.scaleConnWeightModels = {'Izhi2007b': 0.01, 'HH_reduced': 0.005, 'HH_full': 0.005}  # scale conn weight factor for each cell model
netParams.scaleConnWeightNetStims = 1.0 #0.5  # scale conn weight factor for NetStims
netParams.defaultDelay = 5.0 # default conn delay (ms)
netParams.propVelocity = 500.0 # propagation velocity (um/ms)
netParams.probLambda = 100.0  # length constant (lambda) for connection probability decay (um)



# Cell parameters
SimpSecD = {}
SimpSecD['alldend'] = ['Adend2'] # ['Adend1', 'Adend2', 'Adend3', 'Bdend']
SimpSecD['apicdend'] = ['Adend1', 'Adend2', 'Adend3']
SimpSecD['perisom'] = ['soma']

## PT cell params (full)
cellRule = netParams.importCellParams(label='PT_full',conds={'cellType': 'PT', 'cellModel': 'HH_full'},
  fileName='cells/PTcell.hoc', cellName='PTcell', cellArgs = [0, 0,0])
for secName,sec in cellRule['secs'].iteritems(): sec['vinit'] = -70.0432010302


## create list of populations, where each item contains a dict with the pop params
netParams.popParams['PT_L5B'] =	{'cellModel':'HH_full', 'cellType':'PT', 'numCells':1}
netParams.popParams['bgPT'] = {'cellModel': 'NetStim', 'noise': 0.2, 'rate': 20, 'start':0}


# Synaptic mechanism parameters
netParams.synMechParams['AMPA'] = {'mod':'MyExp2SynBB','tau1':0.05,'tau2':5.3,'e':0}
netParams.synMechParams['NMDA'] = {'mod':'MyExp2SynNMDABB','tau1NMDA':15,'tau2NMDA':150,'e':0}
netParams.synMechParams['GABAA'] = {'mod':'MyExp2SynBB','tau1':0.07,'tau2':18.2,'e':-80}
netParams.synMechParams['GABAASlow'] = {'mod':'MyExp2SynBB','tau1':2,'tau2':100,'e':-80}
netParams.synMechParams['GABAASlowSlow'] = {'mod':'MyExp2SynBB','tau1':200,'tau2':400,'e':-80}
netParams.synMechParams['GABAB'] = {'mod':'GABAB'}

ESynMech = ['AMPA', 'NMDA'] 
ISlowSynMech = ['GABAASlow','GABAB']
IFastSynMech = ['GABAA']


# Connectivity rules/params
synWeightFraction = [0.9, 0.1]


netParams.connParams['bg'] = {'preConds': {'popLabel': 'bgPT'}, 
	                          'postConds': {'cellType': 'PT'},
	                          'sec': 'all',
	                          'synMech': ['AMPA', 'NMDA'],
	                          'weight': 0.5,
	                          'loc': 0.5,
	                          'delay': 'max(defaultDelay, gauss(5,3))'}

