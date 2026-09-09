# Synaptic Event and Postsynaptic Potential

# syn = h.ExpSyn(...)
# Represents an excitatory/inhibitory synapse described by an exponential conductance change.

# stim = h.NetStim(...)
# Generates an artificial event at a chosen time.


# nc = h.NetCon(...)
# Connect the event source to the synapse

# Basic Architecture:
# NetStim ->(NetCon)-> ExpSyn ->(postsynaptic neuron)   

from neuron import h
import matplotlib.pyplot as plt
h.load_file("stdrun.hoc")

# 1. CREATE A SIMPLE NEURON

# Soma:
soma = h.Section(name="soma")
soma.L = 20
soma.diam = 20
soma.nseg = 1

# Use a passive membrane (so experiment focuses on synaptic event not on AP)

soma.insert("pas")
soma.Ra = 100 # axial resistance, ohm*cm
soma.cm = 1   # membrane capacitance, uF/cm2

soma.g_pas = 0.0001  # passive leak conductance, S/cm2
soma.e_pas = -65     # resting/reversal potential of passive leak, mV

# 2. CREATE THE SYNAPSE

syn = h.ExpSyn(soma(0.5)) # Create an exponential synapse at the center of the soma
syn.tau = 2 # Time constant of the synaptic conductance (tau is in ms)

# Conductance decays exponentially: g_syn(t) ~ exp(-t/tau)

# 3. CREATE THE EVENT SOURCE

# NetStim is an artificial event generator.
#
# It does NOT directly inject current into the neuron.
#
# Instead, it produces discrete events:
#
#     event at 100 ms
#     event at 200 ms
#     event at 300 ms
#
# Those events can then be sent through a NetCon.

stim = h.NetStim() # Synaptic current is genrated by:  I_syn = g_syn * (V - E_syn)
# the current membrane changes the membrane voltage according to the membrane dynamics:
# for passive membrane:  C_m dV/dt = -I_leak - I_syn 
# with: I_leak = g_pas * (V - E_pas)
# the Postsynaptic Potential (PSP) is the change in membrane voltage produced by the synaptic current.

stim.start = 100 # First event occurs 100ms after simulation starts
stim.number = 1 # Number of events to generate
stim.interval = 100 # How fat apart the events are

# 4. CONNECT THE EVENT SOURCE TO THE SYNAPSE

# NetCon creates the communication between an event source and a target
# First argument is source, the second is the target
# Weight controls the strength of the ysnaptic event (The larger = Larger synaptic conductance = larger PSP)

nc = h.NetCon(stim,syn)
nc.weight[0] = 0.001

# 5. RECORD MEMBRANE VOLTAGE AND TIME

voltage = h.Vector()
voltage.record(soma(0.5)._ref_v) # Record voltage at the middle of the soma

time = h.Vector()
time.record(h._ref_t)

# 6. INITIALIZE AND RUN THE SIMULATION

h.finitialize(-65) # initialize the membrane potential 
h.continuerun(300) # run until 300 ms

# 7. CONVERT NEURON VECTORS TO PYTHON LISTS

time_data = list(time)
voltage_data = list(voltage)

# 8. PLOT THE POSTSYNAPTICPOTENTIAL 

plt.figure(figsize=(9, 5))

plt.plot(time_data, voltage_data)

plt.axvline(
    stim.start,
    linestyle="--",
    label="Synaptic event"
)

plt.xlabel("Time (ms)")
plt.ylabel("Membrane voltage (mV)")
plt.title("Postsynaptic Potential produced by an ExpSyn")

plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# 9. PRINT RESULTS 

resting_voltage = voltage_data[0]
maximum_voltage = max(voltage_data)
psp_amplitude = maximum_voltage - resting_voltage

print("\n===== SYNAPTIC EVENT RESULTS =====")
print(f"Resting voltage: {resting_voltage:.2f} mV")
print(f"Maximum voltage: {maximum_voltage:.2f} mV")
print(f"PSP amplitude:   {psp_amplitude:.4f} mV")
print(f"Synaptic event:  {stim.start:.1f} ms")

# Not neccesarily, we should be observed an action potential, since we used passive membranes
# An event in NEURON is basically a timestamped signal: "Something happened at this instant."
# How does ExpSyn know what to do with the event?
# ExpSyn has its own mathematical model: simplification: gsyn(t) -> gsyn(t) + weight 
# ExpSyn makes conductance decay expotentially: gsyn(t) ~ exp(-t/tau)
# The conductance will create a current: Isyn(t) = gsyn(t) * (V - Esyn)

# EVENT ->change in synaptic conductance -> synaptic current -> change in membrane voltage -> PSP
# the weight also increases the conductance change if you increase it

# To create something more similar to an AP, often the events should be more close up together so that the PSP overlap
# Then accumulated depolarization can reach threshold (TEMPORAL SUMMATION)
# Or we can create more than one synapse (SPATIAL SUMMATION)

