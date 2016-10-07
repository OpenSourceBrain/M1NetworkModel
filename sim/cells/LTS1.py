from neuron import h
from math import sqrt,pi

###############################################################################
# LTS Cell
###############################################################################
class LTS1 ():
  "1-compartment LTS cell"
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

  def set_conductances(self):
    soma = self.soma
    Tfactor=0.0002
    Ttau=0.0
    Hfactor=0.000001
    Htau=0.003
    # kv.mod, na2_mh.mod, cal_mh.mod, kca.mod, cat_traub.mod, ar_traub.mod
    # for ioc in ['pas', 'kv', 'na', 'ca', 'cadad', 'kca', 'catt', 'ar']: soma.insert(ioc)
    # soma.taur_cadad = 20 
    # soma.g_pas=.00007
    # soma.e_pas=-74 
    # #soma.ek = -60
    # soma.ek = -90 + 10
    # soma.ena=  75 - 20
    # soma.vshift_na=-18
    # soma.eca = 140 # from original Mainen patdemo code
    # h.ion_style("ca_ion",0,1,0,0,0)   # from original Mainen patdemo code
    # soma.gbar_ar=Hfactor
    # soma.gbar_na = 7000 * 0.5
    # soma.gmax_kv = 350 * 0.5
    # soma.gbar_ca = 30 * 0.5
    # soma.gmax_kca = 5 * 0.5
    # soma.gbar_catt=Tfactor
