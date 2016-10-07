# simplified corticostriatal cell model (6 compartment)
from neuron import h

Vrest = -80.1220846059
h.v_init = -85.4137121841
h.celsius     = 34.0 # for in vitro opt

# these are to be used by h_kole.mod
h_aslope = 8.60141233799
h_ascale  =  0.00187536380243
h_bslope  =  23.5499534933
h_bscale  =  0.269618020834
h_ashift  =  124.768772141

# geom properties
somaL = 23.9455831784
somaDiam = 44.3019239989
axonL = 645.793181416
axonDiam =  0.401349947627
apicL = 293.606258936
apicDiam = 2.10072357813
bdendL = 229.365228526
bdendDiam = 1.09982284443

# passive properties 
axonCap =  2.08396763682
somaCap =  1.89133252551
apicCap = 2.49636095784
bdendCap = 2.49995878652
rall = 85.1389160393
axonRM = 1046.05518722
somaRM = 7274.88168814
apicRM = 21479.5887648
bdendRM = 11763.9607778

# Na, K reversal potentials calculated from BenS internal/external solutions via Nernst eq.
p_ek = -104.0 # these reversal potentials for in vitro conditions
p_ena = 42.0 
# h-current
h.erev_h = h.erev_ih = -37.0 # global
gbar_h = 1.61656097318e-05

# spiking currents
gbar_nax = 0.0538908368265
nax_gbar_axonm = 5.0
gbar_kdr = 0.019690609625
kdr_gbar_axonm = 5.0
# A few kinetic params changed vis-a-vis kdr.mod defaults:
h.a0n_kdr     = 0.0075 # def 0.02
h.nmax_kdr    = 20.0 # def 2
h.vhalfn_kdr = 11.6427471384
gbar_kap = 0.127795324821
kap_gbar_axonm = 5.0
# A few kinetic params changed vis-a-vis kap.mod defaults:
h.vhalfn_kap  = 42.6103053715
h.nmin_kap    = 0.4 # def 0.1
h.lmin_kap    = 5.0 # def 2
h.tq_kap      = -48.7741740888
h.vhalfl_kap = -30.0952315496

# other ion channel parameters 
cal_gcalbar = 6.27406319558e-06
can_gcanbar = 2.3881757857e-06
cat_gcatbar = 1.10231531492e-06
calginc = 1.0
kBK_gpeak = 3.93910496784e-05
kBK_caVhminShift = 63.7577120517
cadad_depth = 0.0758798224862
cadad_taur = 2.50835513312

gbar_nap = 0.0
gbar_ican = 0.0
			
###############################################################################
# CSTR6 Cell
###############################################################################
class CSTR6 ():
  "Simplified Corticostriatal Cell Model"
  def __init__(self,x=0,y=0,z=0,ID=0):
    self.x,self.y,self.z=x,y,z
    self.ID=ID
    self.all_sec = []
    self.add_comp('soma')
    self.set_morphology()
    self.insert_conductances()
    self.set_props()
    self.calc_area()

  def add_comp(self, name):
    self.__dict__[name] = h.Section(name=name)#,cell=self)
    self.all_sec.append(self.__dict__[name])

  def calc_area(self):
    self.total_area = 0
    self.n = 0
    for sect in self.all_sec:
      self.total_area += h.area(0.5,sec=sect)
      self.n+=1

  def set_morphology(self):
    self.add_comp('axon')
    self.add_comp('Bdend')
    self.add_comp('Adend1')
    self.add_comp('Adend2')
    self.add_comp('Adend3')
    self.apic = [self.Adend1, self.Adend2, self.Adend3]
    self.basal = [self.Bdend]
    self.alldend = [self.Adend1, self.Adend2, self.Adend3, self.Bdend]
    self.set_geom()
    self.axon.connect(self.soma, 0.0, 0.0)
    self.Bdend.connect(self.soma,      0.5, 0.0) # soma 0.5 to Bdend 0
    self.Adend1.connect(self.soma,   1.0, 0.0)
    self.Adend2.connect(self.Adend1,   1.0, 0.0)
    self.Adend3.connect(self.Adend2,   1.0, 0.0)

  def set_geom (self):
    self.axon.L = axonL; self.axon.diam = axonDiam;
    self.soma.L = somaL; self.soma.diam = somaDiam
    for sec in self.apic: sec.L,sec.diam = apicL,apicDiam
    self.Bdend.L = bdendL; self.Bdend.diam = bdendDiam

  def activeoff (self):
    for sec in self.all_sec: sec.gbar_nax=sec.gbar_kdr=sec.gbar_kap=0.0

  def set_axong (self):
    axon = self.axon
    axon.gbar_nax = gbar_nax * nax_gbar_axonm
    axon.gbar_kdr = gbar_kdr * kdr_gbar_axonm
    axon.gbar_kap = gbar_kap * kap_gbar_axonm

  def set_calprops (self,sec):
    sec.gcalbar_cal = cal_gcalbar 
    sec.gcanbar_can = can_gcanbar 
    sec.gcatbar_cat = cat_gcatbar
    sec.gpeak_kBK = kBK_gpeak
    sec.caVhmin_kBK = -46.08 + kBK_caVhminShift
    sec.depth_cadad = cadad_depth
    sec.taur_cadad = cadad_taur   
    sec.gbar_ican = gbar_ican

  def set_somag (self):
    sec = self.soma
    sec.gbar_ih = gbar_h # Ih
    self.set_calprops(sec)
    sec.gbar_nap = gbar_nap

  def set_bdendg (self): 
    sec = self.Bdend
    sec.gbar_ih = gbar_h # Ih
    sec.gbar_nap = gbar_nap
    self.set_calprops(sec)

  def set_apicg (self):
    for sec in self.apic:
      self.set_calprops(sec)
      sec.gbar_ih = gbar_h
      sec.gbar_nap = gbar_nap
    self.apic[1].gcalbar_cal = cal_gcalbar * calginc # middle apical dend gets more iL

  def set_ihkinetics (self):
    for sec in [self.soma,self.Bdend,self.Adend1,self.Adend2,self.Adend3]:
      sec.ascale_ih = h_ascale
      sec.bscale_ih = h_bscale
      sec.ashift_ih = h_ashift
      sec.aslope_ih = h_aslope
      sec.bslope_ih = h_bslope

  # set properties
  def set_props (self):
    self.set_geom()
    # cm - can differ across locations
    self.axon.cm = axonCap
    self.soma.cm = somaCap
    self.Bdend.cm = bdendCap
    for sec in self.apic: sec.cm = apicCap
    # g_pas == 1.0/rm - can differ across locations
    self.axon.g_pas = 1.0/axonRM
    self.soma.g_pas = 1.0/somaRM
    self.Bdend.g_pas = 1.0/bdendRM
    for sec in self.apic: sec.g_pas = 1.0/apicRM
    for sec in self.all_sec:
      sec.ek = p_ek # K+ current reversal potential (mV)
      sec.ena = p_ena # Na+ current reversal potential (mV)
      sec.Ra = rall; sec.e_pas = Vrest # passive      
      sec.gbar_nax    = gbar_nax # Na      
      sec.gbar_kdr    = gbar_kdr # KDR      
      sec.gbar_kap    = gbar_kap # K-A
    # self.set_somag()
    # self.set_bdendg()
    # self.set_apicg()
    # self.set_axong()
    # self.set_ihkinetics()

  def insert_conductances (self):
    for sec in self.all_sec:
      sec.insert('k_ion')
      sec.insert('na_ion')
      sec.insert('pas') # passive
      sec.insert('nax') # Na current
      sec.insert('kdr') # K delayed rectifier current
      sec.insert('kap') # K-A current
    for sec in [self.Adend3, self.Adend2, self.Adend1, self.Bdend, self.soma]:
      sec.insert('ih') # h-current      
      sec.insert('ca_ion') # calcium channels
      sec.insert('cal') # cal_mig.mod
      sec.insert('can') # can_mig.mod
      sec.insert('cat') # cat_mig.mod
      sec.insert('cadad') # cadad.mod - calcium decay 
      sec.insert('kBK') # kBK.mod - ca and v dependent k channel
      sec.insert('nap') # nap_sidi.mod
      sec.insert('ican') # ican_sidi.mod

#
def prmstr (p,s,fctr=2.0,shift=5.0):
  if p == 0.0:
    print s,'=',str(p-shift),str(p+shift),str(p),'True'
  elif p < 0.0:
    print s, '=',str(p*fctr),str(p/fctr),str(p),'True'
  else:
    print s, ' = ' , str(p/fctr), str(p*fctr), str(p), 'True'

