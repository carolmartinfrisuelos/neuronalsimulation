#ADDED 3 DENDRITES IN DIFFERENT GEOMETRY AND CHANGED THE SODIUM CONDUCTANCES

from neuron import h
import matplotlib.pyplot as plt
h.load_file("stdrun.hoc") 

# Create NEURON sections
soma = h.Section(name="soma")

dend1 = h.Section(name="dend1")
dend2 = h.Section(name="dend2")
dend3 = h.Section(name="dend3")

axon = h.Section(name="axon")

# Set morphology
soma.L = 20
soma.diam = 20

axon.L = 1000
axon.diam = 1

dend1.L = 300
dend1.diam = 2

dend2.L = 300
dend2.diam = 2

dend3.L = 300
dend3.diam = 2

# Connect the neuron
dend1.connect(soma(0))
dend2.connect(soma(0))
dend3.connect(dend1(1))

axon.connect(soma(1))

 #               dend3
 #                 |
 #                 |
 #               dend1
 #                 |
 #                 |
 #       dend2 --- soma -------- axon

# Insert Hodgkin-Huxley active channels
# here i took out the normal loop, so the Axial Resistiviy (Ra) 
#and the specific membrane capacitance (cm) 
#But normally, the lipid bilayer itself has a relatively similar specific capacitance.
#What changes dramatically is the geometry and, in some neurons, the myelination.
#For example, myelinated axons can have very different effective electrical properties.

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

#DENDRITE 2
dend2.insert("hh")
dend2.Ra = 100
dend2.cm = 1
dend2.nseg = 11
dend2.gnabar_hh = 0.05

#DENDRITE 3
dend3.insert("hh")
dend3.Ra = 100
dend3.cm = 1
dend3.nseg = 11
dend3.gnabar_hh = 0.05

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
voltage_dend2 = h.Vector()
voltage_dend3 = h.Vector()


# Record time
time.record(h._ref_t)

# Record voltage
voltage_soma.record(soma(0.5)._ref_v)

voltage_axon.record(axon(0.5)._ref_v)

voltage_dend1.record(dend1(0.5)._ref_v)

voltage_dend2.record(dend2(0.5)._ref_v)

voltage_dend3.record(dend3(0.5)._ref_v)


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

dend2_data = list(voltage_dend2)

dend3_data = list(voltage_dend3)


# Find maximum and minimum voltages
max_soma_voltage = max(soma_data)
min_soma_voltage = min(soma_data)

max_axon_voltage = max(axon_data)
min_axon_voltage = min(axon_data)

max_dend1_voltage = max(dend1_data)
min_dend1_voltage = min(dend1_data)

max_dend2_voltage = max(dend2_data)
min_dend2_voltage = min(dend2_data)

max_dend3_voltage = max(dend3_data)
min_dend3_voltage = min(dend3_data)


# Find indexes
max_soma_index = soma_data.index(max_soma_voltage)
min_soma_index = soma_data.index(min_soma_voltage)

max_axon_index = axon_data.index(max_axon_voltage)
min_axon_index = axon_data.index(min_axon_voltage)

max_dend1_index = dend1_data.index(max_dend1_voltage)
min_dend1_index = dend1_data.index(min_dend1_voltage)

max_dend2_index = dend2_data.index(max_dend2_voltage)
min_dend2_index = dend2_data.index(min_dend2_voltage)

max_dend3_index = dend3_data.index(max_dend3_voltage)
min_dend3_index = dend3_data.index(min_dend3_voltage)


# Find corresponding times
max_soma_time = time_data[max_soma_index]
min_soma_time = time_data[min_soma_index]

max_axon_time = time_data[max_axon_index]
min_axon_time = time_data[min_axon_index]

max_dend1_time = time_data[max_dend1_index]
min_dend1_time = time_data[min_dend1_index]

max_dend2_time = time_data[max_dend2_index]
min_dend2_time = time_data[min_dend2_index]

max_dend3_time = time_data[max_dend3_index]
min_dend3_time = time_data[min_dend3_index]


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


print("\nDENDRITE 2")

print(
    f"Maximum voltage: {max_dend2_voltage:.3f} mV "
    f"at {max_dend2_time:.3f} ms"
)

print(
    f"Minimum voltage: {min_dend2_voltage:.3f} mV "
    f"at {min_dend2_time:.3f} ms"
)


print("\nDENDRITE 3")

print(
    f"Maximum voltage: {max_dend3_voltage:.3f} mV "
    f"at {max_dend3_time:.3f} ms"
)

print(
    f"Minimum voltage: {min_dend3_voltage:.3f} mV "
    f"at {min_dend3_time:.3f} ms"
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

plt.plot(
    time_data,
    dend2_data,
    label="Dendrite 2"
)

plt.plot(
    time_data,
    dend3_data,
    label="Dendrite 3"
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

plt.scatter(
    max_dend2_time,
    max_dend2_voltage
)

plt.scatter(
    max_dend3_time,
    max_dend3_voltage
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

plt.scatter(
    min_dend2_time,
    min_dend2_voltage
)

plt.scatter(
    min_dend3_time,
    min_dend3_voltage
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

plt.text(
    max_dend2_time,
    max_dend2_voltage,
    f"Dend2 max: {max_dend2_voltage:.1f} mV"
)

plt.text(
    max_dend3_time,
    max_dend3_voltage,
    f"Dend3 max: {max_dend3_voltage:.1f} mV"
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

plt.text(
    min_dend2_time,
    min_dend2_voltage,
    f"Dend2 min: {min_dend2_voltage:.1f} mV"
)

plt.text(
    min_dend3_time,
    min_dend3_voltage,
    f"Dend3 min: {min_dend3_voltage:.1f} mV"
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