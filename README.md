# M1NetworkModel
## Description
A multiscale model of mouse primary motor cortex (M1)

The code is based on a NEURON/Python-based modularized framework for network simulations with MPI. Using this modularized structure, user can define different models (including cell types, populations, connectivities, etc.) just by modifying a single parameters file. Additionally, the framework allows to store a single data file the following:

1. model specifications (conn rules etc), 

2. network instantiation (list of all cells, connections, etc), 

3. simulation parameter (duration, dt, etc) and output spikes. 

The data file is available in Pickle, JSON and Matlab formats

Two example models are provided: 

1. mpiHHTut.py - simple tutorial model with a single Hodgkin-Huxley population and random connectivity

2. M1_yfrac_izhi.py - mouse M1 model with 14 populations; size 300um x 300um x 1350um, has 10,734 Izhikevich cells, 3,963,006 synapses, and cortical depth-dependent connectivity based on multiple published experimental studies.

Select which model to run by modifying the initialize call in init.py, eg.:

    `s.sim.initialize(                   
        simConfig = M1_yfrac_izhi.simConfig, 
        netParams = M1_yfrac_izhi.netParams)`
        
Additional details of the modelling framework and M1 model can be found here:

* [SFN'15 poster](http://neurosimlab.org/salvadord/sfn15-sal-final.pdf)

* [slides](https://drive.google.com/file/d/0B8v-knmZRjhtVl9BOFY2bzlWSWs/view?usp=sharing)       
 
       

## Setup and execution

Requires NEURON with Python and MPI support. 

1. Type or `./compile or the equivalent `nrnivmodl mod`. This should create a directory called either i686 or x86_64, depending on your computer's architecture. 
2. To run type: `./runsim [num_proc]` or the equivalent `mpiexec -np [num_proc] nrniv -python -mpi init.py`

## Overview of file structure:

* sim/init.py: Main executable; calls functions from other modules. Sets what parameter file to use.

* /params: Contains a single parameters file to define each model. Includes simulation (simConfig) and network (netParams) parameters. 

* /sim/shared.py: Contains all the model shared variables and modules. It is imported as "s" from all other file, so that any variable or module can be referenced from any file using s.varName

* /sim/sim.py: Simulation control functions (eg. runSim).

* /sim/network.py: Network related functions (eg. createCells)

* /sim/cell.py: contains cell and population classes to create cells based on the parameters.

* /sim/analysis.py: functions to visualize and analyse data

* /sim/mod/izhi2007b.mod: NMODL definition of Izhikevich 2007 neuron model

* /data: where the model and simulation data is stored (eg. .pkl, .mat, .json files) 


For further information please contact: salvadordura@gmail.com 

