# Connect 2 neurons through a chemical synapse

# Neuron A
#   │
#   │ action potential
#   ▼
#NetCon
#   │
#   ▼
#Synapse
#   │
#   ▼
#Neuron B

from neuron import h
import matplotlib.pyplot as plt

h.load_file("stdrun.hoc")

# 1. Create Active Neuron 1

cell1 = h.Section(name = "cell1 ")

cell1.L= 20
cell1.diam = 20
cell1.nseg = 1

cell1.insert("hh") # insert active channels

# 2. Create Active Neuron 2

cell2 = h.Section(name = "cell2")
cell2.L= 20
cell2.diam = 20
cell2.nseg = 1

cell2.insert("hh") # insert active channels

# 3. Create a Synapse on Neuron 2

syn = h.ExpSyn(cell2(0.5))
syn.tau = 2
syn.e = 0

"""
Why Synapse on Neuron 2?
- Neuron 1 is presynaptic
- Neuron 2 is postsynaptic

So Neuron 1 is sending the signal to Neuron 2, which is receiving the signal;
Neuron 1 (SENDER)
    |
ACTION POTENTIAL
    |
    ▼
  NetCon
    |
   EVENT
    |
    ▼
  ExpSyn
    |
    ▼
Neuron 2 (RECEIVER)

"""

# 4. Connect Neuron A to Synapse on Neuron B 

nc = h.NetCon(cell1(0.5)._ref_v, syn)

nc.threshold = 0
nc.delay = 1
nc.weight[0]= 0.01

"""
What is NetCon doing?
"Watch the membrane voltage of neuron 1, 
detect when it crosses a threshold [cell1(0.5)._ref_v], 
and send an event to this synapse on neuron 2."

- NetCon = event detector + event transmitter

cell1(0.5)._ref_v: 

cell1
  │
  └── position 0.5
          │
          ▼
       membrane
       voltage


syn: syn = h.ExpSyn(cell2(0.5))

SOURCE                           TARGET

cell1 voltage                    ExpSyn on cell2
     │                                ▲
     │                                │
     └────────── NetCon ──────────────┘


WHEN VOLTAGE CROSSES THRESHOLD (0mV);
NetCon sends EVENT HAPPENED to the synapse on cell2

"""

# 5. Give Neuron 1 Small Stimulus

stim = h.IClamp(cell1(0.5)) 

#At 100 ms, inject current into neuron A for 1 ms. 

stim.delay = 100
stim.dur = 1
stim.amp = 0.1

# 6. Record Voltage from Both Neurons 

t = h.Vector()
v1 = h.Vector()
v2 = h.Vector()

t.record(h._ref_t)

v1.record(cell1(0.5)._ref_v)
v2.record(cell2(0.5)._ref_v)

# 7. Run Simulation

h.finitialize(-65)

h.continuerun(300)

# 8. Plot 

plt.figure(figsize=(16,6))

plt.plot(t, v1, label = "Neuron A")
plt.plot(t, v2, label = "Neuron B")

plt.xlabel ("Time (ms)")
plt.ylabel ("Membrane voltage (mV)")

plt.title("Two-Neuron Synaptic Circuit")
plt.xlim(80, 130) 
# I added it after observing where the AP occured so I can take a better look

plt.grid()
plt.legend()
plt.show()

           



