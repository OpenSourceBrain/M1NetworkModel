import sys
from neuron import h

h.load_file("PTcell.hoc")

#
class PTcell ():
  def __init__ (self):
    self.cell = h.PTcell(0,19,0)
    self.cell.reconfig()

def safereconfig (cell): cell.reconfig()

