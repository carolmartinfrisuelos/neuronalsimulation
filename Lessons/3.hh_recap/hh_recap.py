# Goal is to learn how to modify:

# sec.insert("hh")
# sec.gnabar_hh
# sec.gkbar_hh
# sec.gl_hh
# sec.el_hh
# sec.ena
# sec.ek

# difference between soma.gnabar_hh and soma(0.5).gnabar_hh


from neuron import h
h.load_file("stdrun.hoc") 
import matplotlib.pyplot as plt

# 1. Create the neuron: 

soma = h.Section(name="soma")
dend = h.Section(name="dend")
axon = h.Section(name="axon")

# 2. Define Geometry:

soma.L = 20
soma.diam = 20

dend.L= 300
dend.diam= 2

axon.L= 1000
axon.diam = 1

# 3. Connect the sections

dend.connect(soma(0))
axon.connect(soma(1))

# 4. Define number of segments

soma.nseg = 3
dend.nseg = 11
axon.nseg = 101

# 5. Insert Hodgkin-Huxley Channels

for sec in [soma,dend, axon]:

    sec.insert("hh")

# 6. Basic Membrane Parameters

for sec in [soma,dend,axon]:

    sec.Ra = 100
    sec.cm = 1

# 7. Hodgkin-Huxley Parameters

# Sodium Conductance:

soma.gnabar_hh = 0.12
dend.gnabar_hh = 0.12
axon.gnabar_hh = 0.12

# Potassium Conductance:

soma.gkbar_hh = 0.036
dend.gkbar_hh = 0.036
axon.gkbar_hh = 0.036

# Leak Conductance:

soma.gl_hh = 0.0003
dend.gl_hh = 0.0003
axon.gl_hh = 0.0003

# Leak Reversal Potential:

soma.el_hh = -54.3
dend.el_hh = -54.3
axon.el_hh = -54.3

# Reversal Potentials

# Sodium reversal potential
soma.ena = 50
dend.ena = 50
axon.ena = 50
# Potassium reversal potential
soma.ek = -77
dend.ek = -77
axon.ek = -77


# 8. Show Parameters:

print("\n ===== HODGKIN-HUXLEY PARAMETERS ======")

print("\nSOMA")

print("Na conductance:", soma(0.5).gnabar_hh, "S/cm2")
print("K conductance :", soma(0.5).gkbar_hh, "S/cm2")
print("Leak conductance:", soma(0.5).gl_hh, "S/cm2")
print("Leak reversal:", soma(0.5).el_hh, "mV")

print("\nGlobal reversal potentials")

print("Soma Na reversal:", soma.ena , "mV")
print("Soma K reversal:", soma.ek , "mV")
print("Dendrite Na reversal:", dend.ena, "mV")
print("Dendrite K reversal:", dend.ek, "mV")
print("Axon oma Na reversal:", axon.ena, "mV")
print("Axon K reversal:", axon.ek, "mV")


# 9. Demonstrate Section Vs Segment:

print("\n===== SECTION VS SEGMENT =====")

print("\nUsing the section:")

print(soma.gnabar_hh)


print("\nUsing the middle segment:")

print(soma(0.5).gnabar_hh)

# 10. Current Injection

stim = h.IClamp(soma(0.5))

stim.delay = 100
stim.dur = 800
stim.amp = 0.1

# 11. Recording Vectors

time = h.Vector()

voltage_soma = h.Vector()

voltage_dend = h.Vector()

voltage_axon = h.Vector()


time.record(h._ref_t)

voltage_soma.record(soma(0.5)._ref_v)
voltage_dend.record(dend(0.5)._ref_v)
voltage_axon.record(axon(0.5)._ref_v)

# 12. Simulation Settings:

h.dt = 0.025
h.tstop = 1000
h.finitialize(-65)
h.run()

# 13. Convert NEURON vectors into Python list 

time_data = list(time)
soma_data = list(voltage_soma)
dend_data = list(voltage_dend)
axon_data = list(voltage_axon)

# 14. Plot

plt.figure(figsize=(10,6))

plt.plot(time_data, soma_data, label="Soma")
plt.plot(time_data, dend_data, label="Dendrite")
plt.plot(time_data, axon_data, label="Axon")


plt.xlabel("Time (ms)")

plt.ylabel("Membrane Voltage (mV)")

plt.title("Hodgkin-Huxley Neuron")

plt.legend()

plt.grid(True)

plt.show()


#**Comment: I put the sodium conductance = 0.12 becuase otherwise
# there was a repetitive pattern, and 0.12 follows the classical HH-Model, 
# however, adding an AIS to make higher the conductance in the end of the axon
# maybe could help, or playing with the values