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
stim.amp = 0.05

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

# Find maximum and minimum voltage
max_voltage = max(voltage)
min_voltage = min(voltage)

# Find when they occur
max_index = voltage.index(max_voltage)
min_index = voltage.index(min_voltage)

max_time = time[max_index]
min_time = time[min_index]

print(f"Maximum voltage: {max_voltage:.3f} mV at {max_time:.3f} ms")
print(f"Minimum voltage: {min_voltage:.3f} mV at {min_time:.3f} ms")

# Create figure
plt.figure(figsize=(8,4))

# Plot voltage trace
plt.plot(time, voltage, label="Membrane Voltage")

# Mark maximum voltage
plt.scatter(max_time, max_voltage)
plt.text(
    max_time,
    max_voltage,
    f" Max = {max_voltage:.2f} mV",
    fontsize=9
)

# Mark minimum voltage
plt.scatter(min_time, min_voltage)
plt.text(
    min_time,
    min_voltage,
    f" Min = {min_voltage:.2f} mV",
    fontsize=9
)

# Labels
plt.xlabel("Time (ms)")
plt.ylabel("Membrane Voltage (mV)")
plt.title("Passive Neuron Response")

plt.grid(True)
plt.legend()

plt.show()
