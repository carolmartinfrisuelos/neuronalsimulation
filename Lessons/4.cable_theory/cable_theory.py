# Goal is to understand: 
# A voltage change propagates through the intracellular 
# resistance, and the further you are from the source,
# the more the signal can attenuate

# Inject a voltage/current at one location 
# → measure how much of that voltage reaches different locations along the neuron 
# → see that the signal becomes smaller with distance.


# record: 
# voltage_soma.record(soma(0.5)._ref_v)
# voltage_dend.record(dend(0.5)._ref_v)
# voltage_axon.record(axon(0.5)._ref_v)


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


# 5. Passive Membrane (to understand how volatge decrease or increase without the ion channels)

for sec in [soma, dend, axon]:

    sec.Ra = 100 # Axial Resistance (if higher less propagation)
    sec.cm = 1 # membrane capacitance (how quickly membrane voltage changes)

    sec.insert("pas")

    sec.g_pas = 0.0003 # passive membrane conductance (higher more current leaks through membrane, more voltage attenuation)
    sec.e_pas = -65

# 6. Current Injection

stim = h.IClamp(soma(0.5))

stim.delay = 100
stim.dur = 100
stim.amp = 0.01

# 7. Record Voltage

time = h.Vector()

voltage_soma = h.Vector()
voltage_dend = h.Vector()
voltage_axon = h.Vector()

time.record(h._ref_t)

voltage_soma.record(soma(0.5)._ref_v)
voltage_dend.record(dend(0.5)._ref_v)
voltage_axon.record(axon(0.5)._ref_v)

axon_positions = [0.1, 0.25, 0.5, 0.75, 0.9]

axon_voltage_vectors = []

for pos in axon_positions:
    v = h.Vector()
    v.record(axon(pos)._ref_v)
    axon_voltage_vectors.append(v)

# 8. Simulation

h.dt = 0.025
h.tstop = 500

h.finitialize(-65)
h.run()

# 9. Convert to Python 

time_data = list(time)

soma_data = list(voltage_soma)
dend_data = list(voltage_dend)
axon_data = list(voltage_axon)

# 10. Plot

plt.figure(figsize=(10,6))

plt.plot(time_data, soma_data, label= "Soma")
plt.plot(time_data, dend_data, label= "Dendrite")
plt.plot(time_data, axon_data, label= "Axon")

plt.xlabel("Time(ms)")
plt.ylabel("Membrane Voltage (mV)")
plt.title("Passive Voltage Propagation")

plt.legend()
plt.grid()

plt.show()

# Theoretically:

# Soma: largest voltage change because you inject here voltage
# Dendrite: voltage reaches dendrite but is smaller
# Axon: because axon is long and thin the voltage can attenuate substantially

# 11. Plot the recorded voltage along the axon
# We check attenuation


print("\n===== VOLTAGE ALONG AXON =====")

for pos, voltage_vector in zip(axon_positions, axon_voltage_vectors):
    # zip is a pairing tool

    voltage_data = list(voltage_vector)

    print(
        f"Axon position {pos:.2f}: "
        f"maximum voltage = {max(voltage_data):.3f} mV"
    )