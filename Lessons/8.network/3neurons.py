# 3 cells as a network

""" 
Architecture:

              NetCon             NetCon
CELL 0 ─────────────→ CELL 1 ─────────────→ CELL 2
  │                     │                     │
  │                     │                     │
  AP(IClamp)            AP                    AP

  

- Cell 1 is both postsynaptic and presynaptic
"""

from neuron import h
import matplotlib.pyplot as plt

h.load_file("stdrun.hoc")

# ============================================================
# 1. Function to Create one Neuron
# ============================================================

def create_cell():

    cell = h.Section()

    cell.L = 20
    cell.diam = 20
    cell.nseg = 1

    cell.insert("hh") 

    return cell


# ============================================================
# 2. Create 3 Neurons and store them in a list
# ============================================================

cells = []

for i in range(3):

    cells.append(create_cell()) # use function created above


# name the cells for clarity
cell0 = cells[0]
cell1 = cells[1]
cell2 = cells[2]

# ============================================================
# 3. Create Synapses 
# ============================================================

# From Cell 0 -> Cell 1

# expsyn for receiving signals
syn01 = h.ExpSyn(cell1(0.5)) # converts an arriving event into a conductance change
syn01.tau = 2 
syn01.e = 0


nc01 = h.NetCon(
    cell0(0.5)._ref_v,
    syn01,
    sec=cell0
)

# connects the presynaptic event to the synapse

nc01.threshold = 0
nc01.delay = 1
nc01.weight[0] = 0.04

# netcon: watches voltage from cell0 at 0.5 and send detected events to syn01


# From Cell 1 -> Cell 2

syn12 = h.ExpSyn(cell2(0.5))
syn12.tau = 2
syn12.e  = 0

nc12 = h.NetCon(
    cell1(0.5)._ref_v,
    syn12,
    sec=cell1 # Which Section does this voltage pointer belong to?
    # watching the voltage of the section so if it crosses the threshold it transmits the synapse
)

nc12.threshold = 0
nc12.delay = 1
nc12.weight[0] = 0.05

# ============================================================
# 4. Stimulate Cell 0 with an IClamp
# ============================================================

stim = h.IClamp(cell0(0.5))

stim.delay = 100
stim.dur = 1
stim.amp = 0.1

#=============================================================
# 5. Record Voltage of 3 cells 
#=============================================================

t = h.Vector()

v0 = h.Vector()
v1 = h.Vector()
v2 = h.Vector()

t.record(h._ref_t)

v0.record(cell0(0.5)._ref_v)
v1.record(cell1(0.5)._ref_v)
v2.record(cell2(0.5)._ref_v)

#==============================================================
# 6. Run Simulation
#===============================================================

h.finitialize(-65)

h.continuerun(300)

#==============================================================
# 7. Plot
#===============================================================

plt.figure(figsize=(14, 6))

plt.plot(t, v0, label="Cell 0")
plt.plot(t, v1, label="Cell 1")
plt.plot(t, v2, label="Cell 2")

plt.xlabel("Time (ms)")
plt.ylabel("Membrane voltage (mV)")

plt.title("Three-Neuron Chain")

plt.xlim(80, 180)

plt.legend()
plt.grid()

plt.show()