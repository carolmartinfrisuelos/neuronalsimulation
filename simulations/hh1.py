# HH classical model workflow

from neuron import h
import matplotlib.pyplot as plt
h.load_file("stdrun.hoc") #is a file that comes with NEURON defining tstop, run(), finitialize()

#=======================================================================================================
# 1 create soma, dendrite and axon 
#========================================================================================================

soma= h.Section(name="soma")
axon= h.Section(name="axon")
dend= h.Section(name="dendrite")

#=========================================================================================================
# 2 Give each one a geometry.
#=========================================================================================================
soma.L = 20
soma.diam = 20
soma.nseg = 1

axon.L = 1000
axon.diam = 1
axon.nseg = 11

dend.L = 300
dend.diam = 2
dend.nseg = 7

#==========================================================================================================
# 3 Connect them together.
#==========================================================================================================
axon.connect(soma(1))
dend.connect(soma(0))

#==========================================================================================================
# 4 Insert Hodgkin–Huxley active channels into all three.
#==========================================================================================================

for sec in [soma,axon,dend]:
    sec.insert("hh")
    sec.Ra=100
    sec.cm=1

#===========================================================================================================
# 5 Inject current into the soma.
#============================================================================================================

stim = h.IClamp(soma(0.5)) #stim has no special meaning , it is the name of the varible injected
stim.delay = 10
stim.dur = 1
stim.amp = 0.1
#delay, dur and amp belong to the IClamp object


#==============================================================================================================
# 6 Record voltage from the soma, dendrite, and axon simultaneously.
#===============================================================================================================

#aqui estoy creando 4 vectores distintos pero dentro de NEURON 
# por eso pongo la h, pero el nombre del vectro es time/ voltage soma....

time = h.Vector()

voltage_soma = h.Vector()
voltage_axon = h.Vector()
voltage_dend = h.Vector()

#.record sirve para guardar valores en el vector cada vez que la simulacvion avanza

time.record(h._ref_t)# la 't' en NEURON es la simulation time, 
#entonces _ref_t hace referencia a la current simulation time

#estas diciendo donde esta el voltage de referencia para que NEURON lo monitoree
#en el 0.5 es en el punto medio de la seccion

voltage_soma.record(soma(0.5)._ref_v) 
voltage_axon.record(axon(0.5)._ref_v)
voltage_dend.record(dend(0.5)._ref_v)
#this method records simulations at time steps
#YOU COULD SPECIFY THE RECORDING INTERVAL BY:
# voltage_soma.record(soma(0.5)._ref_v, 0.1), it records every 0.1ms


# initialiaze the simulation

h.finitialize(-65)
h.dt = 0.025 #TIME STEP OF RECORD IN NEURON, ALTHOUGH IT IS NOT NEEDED BUT CAN BE MODIFIED
h.tstop = 100
h.run()

#convert neuron vectors to PYTHON LISTS
#Python lists can easily store different types of objects and they are very flexible
#for mathematical operantions we will often use the NumPy arrays, but now is not needed we only need Matplotlib
time_data = list(time)
soma_data = list(voltage_soma)
axon_data = list(voltage_axon)
dend_data = list(voltage_dend)

#==================================================================================
# 7 Find the maximum and minimum voltage in each.
#====================================================================================

# FIND MAXIMUM AND MINIMUM VOLTAGES
max_soma = max(soma_data)
min_soma = min(soma_data)

max_axon = max(axon_data)
min_axon = min(axon_data)

max_dend = max(dend_data)
min_dend = min(dend_data)

# FIND THE INDICES OF MAXIMUM AND MINIMUM VOLTAGES
#the index tell us the position of the value we want inside the list
max_soma_index = soma_data.index(max_soma)
min_soma_index = soma_data.index(min_soma)

max_axon_index = axon_data.index(max_axon)
min_axon_index = axon_data.index(min_axon)

max_dend_index = dend_data.index(max_dend)
min_dend_index = dend_data.index(min_dend)

#==========================================================================================
# 8 Find when those maximum and minimum voltages occur
#==========================================================================================

#using the postion of the max and min values inside the list
#we find the value of the time in the same position
max_soma_time = time_data[max_soma_index]
min_soma_time = time_data[min_soma_index]

max_axon_time = time_data[max_axon_index]
min_axon_time = time_data[min_axon_index]

max_dend_time = time_data[max_dend_index]
min_dend_time = time_data[min_dend_index]


print("Simulation completed successfully!")

print("\nSOMA")
print(f"Maximum voltage: {max_soma:.3f} mV")
print(f"Maximum voltage time: {max_soma_time:.3f} ms")
print(f"Minimum voltage: {min_soma:.3f} mV")
print(f"Minimum voltage time: {min_soma_time:.3f} ms")


print("\nAXON")
print(f"Maximum voltage: {max_axon:.3f} mV")
print(f"Maximum voltage time: {max_axon_time:.3f} ms")
print(f"Minimum voltage: {min_axon:.3f} mV")
print(f"Minimum voltage time: {min_axon_time:.3f} ms")

print("\nDENDRITE")
print(f"Maximum voltage: {max_dend:.3f} mV")
print(f"Maximum voltage time: {max_dend_time:.3f} ms")
print(f"Minimum voltage: {min_dend:.3f} mV")
print(f"Minimum voltage time: {min_dend_time:.3f} ms")

#============================================================================================
# 9 Plot all three voltage traces on the same graph.
#============================================================================================

plt.figure(figsize=(10, 6))

# Plot soma voltage

plt.plot(
    time_data,
    soma_data,
    label="Soma"
)


# Plot axon voltage

plt.plot(
    time_data,
    axon_data,
    label="Axon"
)


# Plot dendrite voltage

plt.plot(
    time_data,
    dend_data,
    label="Dendrite"
)

#=======================================================================================
# 10 Mark the maximum and minimum of each section.
#=======================================================================================

plt.scatter(
    max_soma_time,
    max_soma,
    label=f"Soma max = {max_soma:.2f} mV"
)

plt.scatter(
    max_axon_time,
    max_axon,
    label=f"Axon max = {max_axon:.2f} mV"
)

plt.scatter(
    max_dend_time,
    max_dend,
    label=f"Dendrite max = {max_dend:.2f} mV"
)

plt.scatter(
    min_soma_time,
    min_soma,
    label=f"Soma min = {min_soma:.2f} mV"
)

plt.scatter(
    min_axon_time,
    min_axon,
    label=f"Axon min = {min_axon:.2f} mV"
)

plt.scatter(
    min_dend_time,
    min_dend,
    label=f"Dendrite min = {min_dend:.2f} mV"
)

plt.xlabel("Time (ms)")

plt.ylabel("Membrane Voltage (mV)")

plt.title("Hodgkin-Huxley Action Potential in Soma, Axon, and Dendrite")

plt.grid(True)

plt.legend()

plt.show()