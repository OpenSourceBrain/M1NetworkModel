## M1 Network Model
### Description
A multiscale model of mouse primary motor cortex (M1).

The code requires the [netpyne package](https://github.com/Neurosim-lab/netpyne), a NEURON/Python-based modularized framework for network simulations with MPI. Using this modularized structure, user can define different models (including cell types, populations, connectivities, etc.) just by modifying a single parameters file. 

Additional details of the modelling framework and M1 model can be found here:

* [SFN'15 poster](http://neurosimlab.org/salvadord/sfn15-sal-final.pdf)
* [slides](https://drive.google.com/file/d/0B8v-knmZRjhtVl9BOFY2bzlWSWs/view?usp=sharing)       
 
The parameter file **M1.py** describes a mouse M1 model with 14 populations; size 300um x 300um x 1350um, has 10,734 Izhikevich cells, 5,029,610 synapses, and cortical depth-dependent connectivity based on multiple published experimental studies.

### Setup and execution

Requires NEURON with Python and MPI support. 

1. Type or `./compile or the equivalent `nrnivmodl mod`. This should create a directory called either i686 or x86_64, depending on your computer's architecture. 
2. To run type: `./runsim [num_proc]` or the equivalent `mpiexec -np [num_proc] nrniv -python -mpi init.py`

The simulation should produce a raster plot with 224,173 spikes (avg rate of 20.88 Hz) over 1 second, showing oscillations in different layers (see below).


![Raster plot](https://raw.githubusercontent.com/OpenSourceBrain/M1NetworkModel/master/raster.png?raw=true "Raster plot of simulation")



### Overview of file structure:

* **M1_run.py**: Main executable; calls functions from other modules. Sets what parameter file to use.

* **M1.py**: Parameters file for M1 Network model. Includes simulation (simConfig) and network (netParams) parameters. 

* **M1_export.py**: Export M1 network to NeuroML

* **izhi2007.py**: Python class (wrapper) for Izhikevich 2007 neuron model

* **izhi2007b.mod**: NMODL definition of Izhikevich 2007 neuron model


For further information please contact: salvadordura@gmail.com or p.gleeson@ucl.ac.uk

