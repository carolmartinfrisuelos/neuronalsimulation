#Plot Time Vs Voltage to answer questions such as:
#When did the stimulus start?
#How large was the voltage change?
#Did the neuron return to rest?
#Did it produce an action potential?

from neuron import h
import matplotlib.pyplot as plt

h.load_file("stdrun.hoc")

# Create sections
soma = h.Section(name="soma")
axon = h.Section(name="axon")
dend = h.Section(name="dendrite")

# Geometry
soma.L = 20
soma.diam = 20

axon.L = 1000
axon.diam = 1

dend.L = 300
dend.diam = 2

# Connections
axon.connect(soma(1))
dend.connect(soma(0))

# Number of segments
soma.nseg = 1
axon.nseg = 101
dend.nseg = 31

# Passive membrane
for sec in [soma, axon, dend]:
    sec.insert("pas")
    sec.Ra = 100
    sec.cm = 1

    for seg in sec:
        seg.pas.g = 0.001
        seg.pas.e = -65

# Current clamp
stim = h.IClamp(soma(0.5))
stim.delay = 10
stim.dur = 50
stim.amp = 0.1

# Recording
v = h.Vector()
t = h.Vector()

v.record(soma(0.5)._ref_v)
t.record(h._ref_t)

# Simulation
h.finitialize(-65)
h.tstop = 100
h.run()

# Convert NEURON vectors to Python lists
time = t.to_python()
voltage = v.to_python()

print("Number of voltage points:", len(voltage))
print("Number of time points:", len(time))

print("First 10 voltage values:")
print(voltage[:10])

print("First 10 time values:")
print(time[:10])

# Plot
plt.figure(figsize=(8, 4))

plt.plot(time, voltage)

plt.xlabel("Time (ms)")
plt.ylabel("Membrane Voltage (mV)")
plt.title("Passive Neuron Response")

plt.grid(True)

plt.show()

print("Neuron created successfully!")