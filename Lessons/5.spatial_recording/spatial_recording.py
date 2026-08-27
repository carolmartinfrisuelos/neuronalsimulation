# record
#  dend(0.1)
# dend(0.3)
# dend(0.5)
# dend(0.7)
# dend(0.9)
# understand positions and nseg


# How voltage changes as I move a long a dendrite

from neuron import h
import matplotlib.pyplot as plt

h.load_file("stdrun.hoc")

# 1. Create Sections

soma = h.Section(name= "soma")
dend = h.Section(name="dend")
axon = h.Section(name= "axon")

# 2. Geometry 

soma.L = 20
soma.diam = 20

dend.L = 300
dend.diam = 2

axon.L = 1000
axon.diam= 1

# 3.  Connect Sections

dend.connect(soma(0))
axon.connect(soma(1))

# 4. Segments 

soma.nseg = 3
dend.nseg = 21
axon.nseg = 51


# 5. Passive Membrane 

for sec in [soma, dend, axon]:

    sec.Ra = 100 
    sec.cm = 1 

    sec.insert("pas")

    sec.g_pas = 0.0003 
    sec.e_pas = -65

# 6. Current Injection

stim = h.IClamp(soma(0.5))

stim.delay = 100
stim.dur = 100
stim.amp = 0.01

# 7. Record Voltage

time = h.Vector()
time.record(h._ref_t)

dend_positions = [0.1, 0.25, 0.5, 0.75, 0.9]

dend_voltage_vectors = []

for pos in dend_positions:

    v = h.Vector()

    v.record(dend(pos)._ref_v)

    dend_voltage_vectors.append(v)


# 8. Simulation

h.dt = 0.025
h.tstop = 500

h.finitialize(-65)
h.run()

# 9. Convert to Python 

time_data = list(time)

# 10. Plot Dendrite

distances = []
voltage_changes = []

for pos, voltage_vector in zip(dend_positions, dend_voltage_vectors):

    voltage_data = list(voltage_vector)

    distance = pos * dend.L
    maximum_voltage = max(voltage_data)

    voltage_change = maximum_voltage - (-65)

    distances.append(distance)
    voltage_changes.append(voltage_change)


plt.figure(figsize=(10, 6))

plt.plot(
    distances,
    voltage_changes,
    marker="o"
)

plt.xlabel("Distance from soma (um)")
plt.ylabel("Voltage change (mV)")
plt.title("Voltage Attenuation Along the Dendrite")

plt.grid()
plt.show()




print("\n===== VOLTAGE ALONG DENDRITE =====")

for pos, voltage_vector in zip(dend_positions, dend_voltage_vectors):

    voltage_data = list(voltage_vector)

    distance = pos * dend.L

    maximum_voltage = max(voltage_data)

    print(
        f"Position: {pos:.2f} | "
        f"Distance: {distance:.1f} um | "
        f"Maximum voltage: {maximum_voltage:.6f} mV"
    )