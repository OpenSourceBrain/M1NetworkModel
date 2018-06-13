import M1  # import parameters file
from netpyne import sim  # import netpyne init module
import math
import sys

np = M1.netParams
np.scale=0.1
np.sizeX = 300*math.sqrt(np.scale) # x-dimension (horizontal length) size in um
np.sizeZ = 300*math.sqrt(np.scale) # z-dimension (horizontal depth) size in um

sc = M1.simConfig
sc.duration = 1000

if '-nogui' in sys.argv:
    import netpyne
    netpyne.__gui__ = False

sim.createSimulateAnalyze(netParams = np, simConfig = sc)  # create and simulate network