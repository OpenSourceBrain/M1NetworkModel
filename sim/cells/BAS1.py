from neuron import h
from math import sqrt,pi

###############################################################################
# Soma-targeting interneuron (fast-spiking Basket Cell -- BAS1)
###############################################################################
class BAS1 ():
  "1-compartment basket cell"	
  def __init__ (self,x,y,z,ID,ty):
    self.soma = h.Section()
    self.x=x
    self.y=y
    self.z=z
    self.ID=ID
    self.ty = ty
    self.set_morphology()
    self.set_conductances()

  def set_morphology(self):
    total_area = 10000 # um2
    self.soma.nseg  = 1
    self.soma.cm    = 1      # uF/cm2
    diam = sqrt(total_area) # um
    L    = diam/pi  # um			
    h.pt3dclear(sec=self.soma)
    h.pt3dadd(self.x, self.y, self.z,   diam, sec=self.soma)
    h.pt3dadd(self.x, self.y, self.z+L, diam, sec=self.soma)
			
  def set_conductances(self): # Bas
    cap         = 1.0
    rall        = 150.0
    rm          = 10e3 
    Vrest       = -79.8
    p_ek          = -85.0 
    p_ena        = 55.0 
    nax_gbar = 0.081
    sh_nax = 0.0
    kdr_gbar = 0.021
    h_gbar = 0.00002
    sec = self.soma
    sec.insert('k_ion')
    sec.insert('na_ion')
    sec.insert('pas') # passive     
    sec.insert('nax') # nax_BS.mod - Na current      
    sec.insert('kdr') # kdr_BS.mod - K delayed rectifier current
    # erev
    sec.ek = p_ek # K+ current reversal potential (mV)
    sec.ena = p_ena # Na+ current reversal potential (mV)
    # passive
    sec.g_pas = 1.0/rm
    sec.Ra = rall
    sec.cm = cap
    sec.e_pas = Vrest
    # Na
    sec.gbar_nax = nax_gbar
    sec.sh_nax = sh_nax
    # KDR
    sec.gbar_kdr = kdr_gbar
    sec.insert('HCN1') # HCN1.mod
    sec(0.5).HCN1.gbar = h_gbar
