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
simConfig.dt = 0.05 # Internal integration timestep to use
simConfig.seeds = {'conn': 1, 'stim': 1, 'loc': 1} # Seeds for randomizers (connectivity, input stimulation and cell locations)
simConfig.createNEURONObj = 1  # create HOC objects when instantiating network
simConfig.createPyStruct = 1  # create Python structure (simulator-independent) when instantiating network
simConfig.verbose = 0 # Whether to write diagnostic information on events 
simConfig.hParams = {'celsius': 34, 'v_init': -65}  # set celsius temp

# Recording 
simConfig.recordCells = [('PT_L5B',0), ('IT_L5A',0), ('IT_L5B',0)]  # list of cells to record from (those selected for plotting below, will be recorded automatically)
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
simConfig.filename = '../data/M1_detailed'  # Set file output name
simConfig.savePickle = False # save to pickle file
simConfig.saveJson = True # save to json file
simConfig.saveMat = False # save to mat file
simConfig.saveDataInclude = ['simData']
simConfig.gatherOnlySimData = True

# Analysis and plotting 
simConfig.addAnalysis('plotRaster', True) # Whether or not to plot a raster
simConfig.addAnalysis('plotTraces', {'include': [('IT_L23',0), ('PT_L5B',1), ('PV_L23',2), ('SOM_L5',3)]}) # plot recorded traces for this list of cells
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

## IT cell params (full)
cellRule = netParams.importCellParams(label='IT_full', conds={'cellType': 'IT', 'cellModel': 'HH_full'},
  fileName='cells/ITcell.hoc', cellName='ITcell', cellArgs = [0, 0,0])
for secName,sec in cellRule['secs'].iteritems(): sec['vinit'] = -70.0432010302

## IT cell params (6-comp)
cellRule = netParams.importCellParams(label='IT_6comp',conds={'cellType': 'IT', 'cellModel': 'HH_reduced'},
  fileName='cells/CSTR6.py', cellName='CSTR6')
for secName,sec in cellRule['secs'].iteritems(): sec['vinit'] = -75.0413649414 
for k in ['alldend', 'apicdend','perisom']: cellRule['secLists'][k] = SimpSecD[k]

## PT cell params (6-comp)
cellRule = netParams.importCellParams(label='PT_6comp',conds={'cellType': 'PT', 'cellModel': 'HH_reduced'},
  fileName='cells/SPI6.py', cellName='SPI6')
for secName,sec in cellRule['secs'].iteritems(): sec['vinit'] = -75.0413649414 
for k in ['alldend', 'apicdend','perisom']: cellRule['secLists'][k] = SimpSecD[k]

## PT cell params (full)
cellRule = netParams.importCellParams(label='PT_full',conds={'cellType': 'PT', 'cellModel': 'HH_full'},
  fileName='cells/PTcell.hoc', cellName='PTcell', cellArgs = [0, 0,0])
for secName,sec in cellRule['secs'].iteritems(): sec['vinit'] = -70.0432010302

## CT cell params (6-comp)
cellRule = netParams.importCellParams(label='CT_6comp',conds={'cellType': 'CT', 'cellModel': 'HH_reduced'},
  fileName='cells/CSTR6.py', cellName='CSTR6')
for secName,sec in cellRule['secs'].iteritems(): sec['vinit'] = -75.0413649414 
for k in ['alldend', 'apicdend','perisom']: cellRule['secLists'][k] = SimpSecD[k]

## SOM cell params
cellRule = netParams.importCellParams(label='SOM', conds={'cellType': 'SOM','cellModel':'HH_reduced'},
  fileName='cells/LTS1.py', cellName='LTS1', cellArgs=[0,0,0,0,0])

## PV cell params
cellRule = netParams.importCellParams(label='PV', conds={'cellType':'PV','cellModel':'HH_reduced'}, 
  fileName='cells/BAS1.py', cellName='BAS1', cellArgs=[0,0,0,0,0])


## create list of populations, where each item contains a dict with the pop params
netParams.addPopParams('CT_L6',		{'cellModel':'HH_reduced',	'cellType':'CT',	'ynormRange':[0.77,1.0],	'density':40e3})
netParams.addPopParams('IT_L6',		{'cellModel':'HH_reduced',	'cellType':'IT',	'ynormRange':[0.77,1.0],	'density':40e3})
netParams.addPopParams('SOM_L6',	{'cellModel':'HH_reduced',	'cellType':'SOM',	'ynormRange':[0.77,1.0],	'density':10e3})
netParams.addPopParams('PV_L6',		{'cellModel':'HH_reduced',	'cellType':'PV',	'ynormRange':[0.77,1.0],	'density':10e3})
netParams.addPopParams('PT_L5B',	{'cellModel':'HH_full',		'cellType':'PT',	'ynormRange':[0.52,0.77],	'density':40e3})
netParams.addPopParams('IT_L5B',	{'cellModel':'HH_full',		'cellType':'IT',	'ynormRange':[0.52,0.77],	'density':40e3})
netParams.addPopParams('IT_L5A',	{'cellModel':'HH_full',		'cellType':'IT',	'ynormRange':[0.41,0.52],	'density':80e3})
netParams.addPopParams('SOM_L5',	{'cellModel':'HH_reduced',	'cellType':'SOM',	'ynormRange':[0.31,0.77],	'density':10e3}) 
netParams.addPopParams('PV_L5',		{'cellModel':'HH_reduced',	'cellType':'PV',	'ynormRange':[0.31,0.77],	'density':10e3})
netParams.addPopParams('IT_L4',		{'cellModel':'HH_reduced',	'cellType':'IT',	'ynormRange':[0.31, 0.41],	'density':80e3})
netParams.addPopParams('IT_L23',	{'cellModel':'HH_reduced',	'cellType':'IT',	'ynormRange':[0.12, 0.31],	'density':80e3})
netParams.addPopParams('SOM_L23',	{'cellModel':'HH_reduced',	'cellType':'SOM',	'ynormRange':[0.12,0.31],	'density':10e3})
netParams.addPopParams('PV_L23',	{'cellModel':'HH_reduced',	'cellType':'PV',	'ynormRange':[0.12,0.31],	'density':10e3})

# Synaptic mechanism parameters
netParams.addSynMechParams('AMPA', {'mod':'MyExp2SynBB','tau1':0.05,'tau2':5.3,'e':0})
netParams.addSynMechParams('NMDA', {'mod':'MyExp2SynNMDABB','tau1NMDA':15,'tau2NMDA':150,'e':0})
netParams.addSynMechParams('GABAA', {'mod':'MyExp2SynBB','tau1':0.07,'tau2':18.2,'e':-80})
netParams.addSynMechParams('GABAASlow', {'mod':'MyExp2SynBB','tau1':2,'tau2':100,'e':-80})
netParams.addSynMechParams('GABAASlowSlow', {'mod':'MyExp2SynBB','tau1':200,'tau2':400,'e':-80})
netParams.addSynMechParams('GABAB', {'mod':'GABAB'})

ESynMech = ['AMPA', 'NMDA'] 
ISlowSynMech = ['GABAASlow','GABAB']
IFastSynMech = ['GABAA']


# Connectivity rules/params
synWeightFraction = [0.9, 0.1]
EtoPTweightFactor = 0.2
netParams.ItoIweight = 0.1

addBackground = 1
addEtoE = 1
addEtoI = 1
addItoEI = 1

with open('../data/conn.pkl', 'r') as fileObj:
    connData = pickle.load(fileObj)

smat = connData['smat']
pmat = connData['pmat']
wmat = connData['wmat']
bins = connData['bins']

####################################################################################################
## Background inputs
####################################################################################################

if addBackground:
	# Create populations of NetStims
	bgNoise = 0.5
	bgRates = {'CT': 10, 'IT': 10, 'PT': 10, 'PV': 10, 'SOM': 10}
 	for postType in ['CT', 'IT', 'PT', 'PV', 'SOM']:
	    bgPopParams = {'cellModel': 'NetStim', 'noise': bgNoise, 'rate': bgRates[postType], 'start':0}
	    netParams.addPopParams('bg'+postType, bgPopParams)

	# Created conn rules between bg->E
	bgWeightsE = {'CT': 0.1, 'IT': 0.1, 'PT': 0.1, 'PV': 0.1, 'COM': 0.1}
	bgWeightsI = {'CT': 0.0, 'IT': 0.0, 'PT': 0.0, 'PV': 0.0, 'COM': 0.0}
  	for postType in ['CT', 'IT', 'PT']: # postsynaptic E cell types  		
  		for mech,sec,wt in zip(['AMPA','GABAA'], ['alldend','perisom'], [bgWeightsE[postType], bgWeightsI[postType]]):
  			netParams.addConnParams(params={'preConds': {'popLabel': 'bg'+postType}, 
	                                      'postConds': {'cellType': postType},
	                                      'sec':sec,
	                                      'synMech': mech,
	                                      'weight': wt,
	                                      'loc': 0.5,
	                                      'delay': 'max(defaultDelay, gauss(5,3))'})  
    
    # Created conn rules between bg->I
  	for poty in ['PV', 'SOM']: # postsynaptic I cells
  		for mech,sec,wt in zip(['AMPA','GABAA'], ['alldend','perisom'], [bgWeightsE[postType], bgWeightsI[postType]]):
  			netParams.addConnParams(params={'preConds': {'popLabel': 'bg'+postType}, 
	                                      'postConds': {'cellType': postType},
	                                      'synMech': mech,
	                                      'weight': wt,
	                                      'loc': 0.5,
	                                      'delay': 'max(defaultDelay, gauss(5,3))'})  

####################################################################################################
## Exc -> Exc
####################################################################################################

if addEtoE:
	labelsConns = [('W+AS_norm', 'IT', 'L2/3'), ('W+AS_norm', 'IT', 'L4,5A,5B'), ('W+AS_norm', 'PT', 'L5B'), ('W+AS_norm', 'IT,CT', 'L6')]
	labelPostBins = [('W+AS', 'IT', 'L2/3'), ('W+AS', 'IT', 'L4,5A,5B'), ('W+AS', 'PT', 'L5B'), ('W+AS', 'IT,CT', 'L6')]
	labelPreBins = ['W', 'AS', 'AS', 'W']
	preTypes = ['IT', 'PT', 'CT']
	postTypes = ['IT', 'IT', 'PT', ['IT,CT']]
	ESynMech = ['AMPA','NMDA']

	for i,(label, preBinLabel, postBinLabel) in enumerate(zip(labelsConns,labelPreBins, labelPostBins)):
		for ipre, preBin in enumerate(bins[preBinLabel]):
			for ipost, postBin in enumerate(bins[postBinLabel]):
				netParams.addConnParams(params={'preConds': {'cellType': preTypes, 'ynorm': preBin},
												'postConds': {'cellType': postTypes[i], 'ynorm': postBin},
												'synMech': ESynMech,
												'probability': pmat[label][ipost,ipre],
												'weight': wmat[label][ipost,ipre],
												'synWeightFraction': synWeightFraction,
												'delay': 'defaultDelay+dist_3D/propVelocity'})

####################################################################################################
## Exc -> Inh
####################################################################################################

if addEtoI:
	labelsConns = ['FS', 'LTS']
	labelPostBins = ['FS/LTS', 'FS/LTS']
	labelPreBins = ['FS/LTS', 'FS/LTS']
	preTypes = ['IT', 'PT', 'CT']
	postTypes = ['PV', 'SOM']
	ESynMech = ['AMPA','NMDA']

	for i,(label, preBinLabel, postBinLabel) in enumerate(zip(labelsConns,labelPreBins, labelPostBins)):
		for ipre, preBin in enumerate(bins[preBinLabel]):
			for ipost, postBin in enumerate(bins[postBinLabel]):
				netParams.addConnParams(params={'preConds': {'cellType': preTypes, 'ynorm': preBin},
												'postConds': {'cellType': postTypes[i], 'ynorm': postBin},
												'synMech': ESynMech,
												'probability': pmat[label][ipost,ipre],
												'weight': wmat[label][ipost,ipre],
												'synWeightFraction': synWeightFraction,
												'delay': 'defaultDelay+dist_3D/propVelocity'})


###################################################################################################
# Inh -> All
###################################################################################################

netParams.addConnParams(params={'preConds': {'popLabel': 'SOM_L23'},
'postConds': {'ynorm': [0.12,0.31]},
'synMech': 'GABAB',
'probability': '1.0 * exp(-dist_3D/probLambda)',
'weight': 'ItoIweight',
'delay': 'defaultDelay+dist_3D/propVelocity',
'synsPerConn': 5,
'sec': 'alldend'})

netParams.addConnParams(params={'preConds': {'popLabel': 'SOM_L5'},
'postConds': {'ynorm': [0.31,0.77]},
'synMech': 'GABAB',
'probability': '1.0 * exp(-dist_3D/probLambda)',
'weight': 'ItoIweight',
'delay': 'defaultDelay+dist_3D/propVelocity',
'synsPerConn': 5,
'sec': 'alldend'})

netParams.addConnParams(params={'preConds': {'popLabel': 'SOM_L6'},
'postConds': {'ynorm': [0.77,1.0]},
'synMech': 'GABAB',
'probability': '1.0 * exp(-dist_3D/probLambda)',
'weight': 'ItoIweight',
'delay': 'defaultDelay+dist_3D/propVelocity',
'synsPerConn': 5,
'sec': 'alldend'})

netParams.addConnParams(params={'preConds': {'popLabel': 'PV_L23'},
'postConds': {'ynorm': [0.12,0.31]},
'synMech': 'GABAA',
'probability': '1.0 * exp(-dist_3D/probLambda)',
'weight': 'ItoIweight',
'delay': 'defaultDelay+dist_3D/propVelocity',
'synsPerConn': 5,
'sec': 'alldend'})

netParams.addConnParams(params={'preConds': {'popLabel': 'PV_L5'},
'postConds': {'ynorm': [0.31,0.77]},
'synMech': 'GABAA',
'probability': '1.0 * exp(-dist_3D/probLambda)',
'weight': 'ItoIweight',
'delay': 'defaultDelay+dist_3D/propVelocity',
'synsPerConn': 5,
'sec': 'alldend'})

netParams.addConnParams(params={'preConds': {'popLabel': 'PV_L6'},
'postConds': {'ynorm': [0.77,1.0]},
'synMech': 'GABAA',
'probability': '1.0 * exp(-dist_3D/probLambda)',
'weight': 'ItoIweight',
'delay': 'defaultDelay+dist_3D/propVelocity',
'synsPerConn': 5,
'sec': 'alldend'})






