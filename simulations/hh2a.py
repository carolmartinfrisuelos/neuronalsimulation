# VERSION OF hh2 bit only Na changed no dendrite geometry

from neuron import h
import matplotlib.pyplot as plt
h.load_file("stdrun.hoc") 

# Create NEURON sections
soma = h.Section(name="soma")

dend1 = h.Section(name="dend1")

axon = h.Section(name="axon")

# Set morphology
soma.L = 20
soma.diam = 20

axon.L = 1000
axon.diam = 1

dend1.L = 300
dend1.diam = 2


# Connect the neuron
dend1.connect(soma(0))

axon.connect(soma(1))

#SOMA
soma.insert("hh")
soma.Ra = 100
soma.cm = 1
soma.nseg = 3
soma.gnabar_hh = 0.12 #insert different sodium conductance

#AXON
axon.insert("hh")
axon.Ra = 100
axon.cm = 1
axon.nseg = 101
axon.gnabar_hh = 0.30

#DENDRITE 1
dend1.insert("hh")
dend1.Ra = 100
dend1.cm = 1
dend1.nseg = 11
dend1.gnabar_hh = 0.05

# Create current clamp
stim = h.IClamp(soma(0.5))

stim.delay = 10
stim.dur = 1
stim.amp = 0.1

# Create recording vectors
time = h.Vector()

voltage_soma = h.Vector()
voltage_axon = h.Vector()

voltage_dend1 = h.Vector()



# Record time
time.record(h._ref_t)

# Record voltage
voltage_soma.record(soma(0.5)._ref_v)

voltage_axon.record(axon(0.5)._ref_v)

voltage_dend1.record(dend1(0.5)._ref_v)


# Simulation settings
h.dt = 0.025
h.tstop = 100

# Initialize membrane voltage
h.finitialize(-65)

# Run simulation
h.run()

# Convert NEURON vectors to Python lists

time_data = list(time)

soma_data = list(voltage_soma)

axon_data = list(voltage_axon)

dend1_data = list(voltage_dend1)



# Find maximum and minimum voltages
max_soma_voltage = max(soma_data)
min_soma_voltage = min(soma_data)

max_axon_voltage = max(axon_data)
min_axon_voltage = min(axon_data)

max_dend1_voltage = max(dend1_data)
min_dend1_voltage = min(dend1_data)


# Find indexes
max_soma_index = soma_data.index(max_soma_voltage)
min_soma_index = soma_data.index(min_soma_voltage)

max_axon_index = axon_data.index(max_axon_voltage)
min_axon_index = axon_data.index(min_axon_voltage)

max_dend1_index = dend1_data.index(max_dend1_voltage)
min_dend1_index = dend1_data.index(min_dend1_voltage)


# Find corresponding times
max_soma_time = time_data[max_soma_index]
min_soma_time = time_data[min_soma_index]

max_axon_time = time_data[max_axon_index]
min_axon_time = time_data[min_axon_index]

max_dend1_time = time_data[max_dend1_index]
min_dend1_time = time_data[min_dend1_index]



print("\nSOMA")

print(
    f"Maximum voltage: {max_soma_voltage:.3f} mV "
    f"at {max_soma_time:.3f} ms"
)

print(
    f"Minimum voltage: {min_soma_voltage:.3f} mV "
    f"at {min_soma_time:.3f} ms"
)


print("\nAXON")

print(
    f"Maximum voltage: {max_axon_voltage:.3f} mV "
    f"at {max_axon_time:.3f} ms"
)

print(
    f"Minimum voltage: {min_axon_voltage:.3f} mV "
    f"at {min_axon_time:.3f} ms"
)


print("\nDENDRITE 1")

print(
    f"Maximum voltage: {max_dend1_voltage:.3f} mV "
    f"at {max_dend1_time:.3f} ms"
)

print(
    f"Minimum voltage: {min_dend1_voltage:.3f} mV "
    f"at {min_dend1_time:.3f} ms"
)



# ============================================================
# CREATE PLOT
# ============================================================

plt.figure(figsize=(12, 7))


# Plot voltage from all sections

plt.plot(
    time_data,
    soma_data,
    label="Soma"
)

plt.plot(
    time_data,
    axon_data,
    label="Axon"
)

plt.plot(
    time_data,
    dend1_data,
    label="Dendrite 1"
)


# ============================================================
# MARK MAXIMUM VOLTAGES
# ============================================================

plt.scatter(
    max_soma_time,
    max_soma_voltage
)

plt.scatter(
    max_axon_time,
    max_axon_voltage
)

plt.scatter(
    max_dend1_time,
    max_dend1_voltage
)


# ============================================================
# MARK MINIMUM VOLTAGES
# ============================================================

plt.scatter(
    min_soma_time,
    min_soma_voltage
)

plt.scatter(
    min_axon_time,
    min_axon_voltage
)

plt.scatter(
    min_dend1_time,
    min_dend1_voltage
)



# ============================================================
# LABEL MAXIMUM VALUES
# ============================================================

plt.text(
    max_soma_time,
    max_soma_voltage,
    f"Soma max: {max_soma_voltage:.1f} mV"
)

plt.text(
    max_axon_time,
    max_axon_voltage,
    f"Axon max: {max_axon_voltage:.1f} mV"
)

plt.text(
    max_dend1_time,
    max_dend1_voltage,
    f"Dend1 max: {max_dend1_voltage:.1f} mV"
)


# ============================================================
# LABEL MINIMUM VALUES
# ============================================================

plt.text(
    min_soma_time,
    min_soma_voltage,
    f"Soma min: {min_soma_voltage:.1f} mV"
)

plt.text(
    min_axon_time,
    min_axon_voltage,
    f"Axon min: {min_axon_voltage:.1f} mV"
)

plt.text(
    min_dend1_time,
    min_dend1_voltage,
    f"Dend1 min: {min_dend1_voltage:.1f} mV"
)


# ============================================================
# GRAPH LABELS
# ============================================================

plt.xlabel("Time (ms)")

plt.ylabel("Membrane Voltage (mV)")

plt.title(
    "Action Potential Propagation in a Neuron "
    "with Soma, Axon, and Three Dendrites"
)

plt.legend()

plt.grid(True)

plt.show()

