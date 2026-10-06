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

# Record voltage from different parts of the neuron
v_soma = h.Vector()
v_axon = h.Vector()
v_dend = h.Vector()

# Record simulation time
t = h.Vector()

v_soma.record(soma(0.5)._ref_v)
v_axon.record(axon(0.5)._ref_v)
v_dend.record(dend(0.5)._ref_v)

t.record(h._ref_t)

# Simulation
h.finitialize(-65)
h.tstop = 100
h.run()

# Convert NEURON vectors to Python lists
time = t.to_python()

voltage_soma = v_soma.to_python()
voltage_axon = v_axon.to_python()
voltage_dend = v_dend.to_python()

# Find maximum and minimum voltage
max_soma = max(voltage_soma)
min_soma = min(voltage_soma)

max_axon = max(voltage_axon)
min_axon = min(voltage_axon)

max_dend = max(voltage_dend)
min_dend = min(voltage_dend)

# Find when they occur
# ---------- SOMA ----------
max_soma = max(voltage_soma)
min_soma = min(voltage_soma)

max_soma_index = voltage_soma.index(max_soma)
min_soma_index = voltage_soma.index(min_soma)

max_soma_time = time[max_soma_index]
min_soma_time = time[min_soma_index]


# ---------- AXON ----------
max_axon = max(voltage_axon)
min_axon = min(voltage_axon)

max_axon_index = voltage_axon.index(max_axon)
min_axon_index = voltage_axon.index(min_axon)

max_axon_time = time[max_axon_index]
min_axon_time = time[min_axon_index]


# ---------- DENDRITE ----------
max_dend = max(voltage_dend)
min_dend = min(voltage_dend)

max_dend_index = voltage_dend.index(max_dend)
min_dend_index = voltage_dend.index(min_dend)

max_dend_time = time[max_dend_index]
min_dend_time = time[min_dend_index]

print()

print("\n========== SOMA ==========")
print(f"Maximum: {max_soma:.3f} mV at {max_soma_time:.3f} ms")
print(f"Minimum: {min_soma:.3f} mV at {min_soma_time:.3f} ms")

print("\n========== AXON ==========")
print(f"Maximum: {max_axon:.3f} mV at {max_axon_time:.3f} ms")
print(f"Minimum: {min_axon:.3f} mV at {min_axon_time:.3f} ms")

print("\n========== DENDRITE ==========")
print(f"Maximum: {max_dend:.3f} mV at {max_dend_time:.3f} ms")
print(f"Minimum: {min_dend:.3f} mV at {min_dend_time:.3f} ms")


plt.figure(figsize=(12,6))

# Plot the three recordings
plt.plot(time, voltage_soma, label="Soma")
plt.plot(time, voltage_axon, label="Axon")
plt.plot(time, voltage_dend, label="Dendrite")


# ---------- SOMA ----------
plt.scatter(max_soma_time, max_soma)
plt.scatter(min_soma_time, min_soma)

plt.text(max_soma_time, max_soma,
         f"S Max\n{max_soma:.2f} mV",
         fontsize=8)

plt.text(min_soma_time, min_soma,
         f"S Min\n{min_soma:.2f} mV",
         fontsize=8)


# ---------- AXON ----------
plt.scatter(max_axon_time, max_axon)
plt.scatter(min_axon_time, min_axon)

plt.text(max_axon_time, max_axon,
         f"A Max\n{max_axon:.2f} mV",
         fontsize=8)

plt.text(min_axon_time, min_axon,
         f"A Min\n{min_axon:.2f} mV",
         fontsize=8)


# ---------- DENDRITE ----------
plt.scatter(max_dend_time, max_dend)
plt.scatter(min_dend_time, min_dend)

plt.text(max_dend_time, max_dend,
         f"D Max\n{max_dend:.2f} mV",
         fontsize=8)

plt.text(min_dend_time, min_dend,
         f"D Min\n{min_dend:.2f} mV",
         fontsize=8)


plt.xlabel("Time (ms)")
plt.ylabel("Membrane Voltage (mV)")
plt.title("Passive Membrane Response")

plt.grid(True)
plt.legend()

plt.show()