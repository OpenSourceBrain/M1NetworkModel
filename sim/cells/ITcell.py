from neuron import h

h.load_file("ITcell.hoc")

# make Ben's cell with additional ion channels
def makecell ():
  cell = h.ITcell(0,19,0)
  return cell


# turn off active conductances (only na, k, but not kdmc)
def activeoff ():
  h.nax_gbar = 0.027 * 0.0
  h.kdr_gbar = 0.007 * 0.0
  h.kap_gbar = 0.1 * 0.0

# turn on active conductances (only na, k - but not kdmc)
def activeon ():
  h.nax_gbar = 0.027 * 1.0
  h.kdr_gbar = 0.007 * 1.0
  h.kap_gbar = 0.1 * 1.0

pc = None

# turn on multisplit
def multispliton (nthread=10):
  pc.change_nthread(nthread, 1)
  pc.multisplit(1)

# turn off multisplit
def multisplitoff ():
  pc.change_nthread(1, 1)
  pc.multisplit(0)

# wrap reconfig with off/on of multisplit
# NB: done to avoid error from recalculation of segment distance from soma, since
#       the number of segments may depend on passive params (via optimize_nseg)
def safereconfig (cell):
  #multisplitoff()
  cell.reconfig()
  #multispliton()

