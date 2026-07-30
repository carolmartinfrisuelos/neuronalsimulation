from neuron import h
import matplotlib.pyplot as plt

h.load_file("stdrun.hoc")


# =====================================================
# CREATE THE NEURON
# =====================================================

soma = h.Section(name="soma")
dend = h.Section(name="dend")
axon = h.Section(name="axon")

# Geometry

soma.L = 20
soma.diam = 20

dend.L = 300
dend.diam = 2

axon.L = 1000
axon.diam = 1

# Connections

dend.connect(soma(0))
axon.connect(soma(1))


# =====================================================
# INSERT HODGKIN-HUXLEY CHANNELS
# =====================================================

for sec in [soma, dend, axon]:

    sec.insert("hh")

    sec.Ra = 100
    sec.cm = 1

# Number of segments

soma.nseg = 3
dend.nseg = 11
axon.nseg = 101


# =====================================================
# FUNCTION
# =====================================================

def run_simulation(current):

    stim = h.IClamp(soma(0.5))

    stim.delay = 10
    stim.dur = 1
    stim.amp = current

    time = h.Vector()
    voltage = h.Vector()

    time.record(h._ref_t)
    voltage.record(soma(0.5)._ref_v)

    h.dt = 0.025
    h.tstop = 40

    h.finitialize(-65)
    h.run()

    return list(time), list(voltage)


# =====================================================
# RUN ONE SIMULATION
# =====================================================

time_data, voltage_data = run_simulation(10)


# =====================================================
# PLOT
# =====================================================

plt.figure(figsize=(8,5))

plt.plot(time_data, voltage_data)

plt.xlabel("Time (ms)")
plt.ylabel("Voltage (mV)")
plt.title("Current Injection")

plt.grid(True)

plt.show()