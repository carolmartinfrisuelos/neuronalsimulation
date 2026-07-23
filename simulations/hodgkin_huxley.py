from neuron import h
import matplotlib.pyplot as plt
h.load_file("stdrun.hoc") #is a file that comes with NEURON defining tstop, run(), finitialize()


# Create the soma
#to simplify the first simulation of action potential we only chose a soma
soma = h.Section(name="soma")

# Set the geometry of the soma
#simplified spherical like compartment
soma.L = 20
soma.diam = 20
soma.nseg = 1 #our section is one entire segment


# Insert the Hodgkin-Huxley mechanism
soma.insert("hh")


# Set the membrane capacitance
soma.cm = 1 #classical value of 1 uF/cm^2


# Set the axial resistance
soma.Ra = 100 # resistance of current to flow inside the cell


# Create a current clamp
stim = h.IClamp(soma(0.5))

# Set stimulation parameters 
stim.delay = 10 # gives the neuron 10ms to reach resting state
stim.dur = 1 #current injected for 1 ms
stim.amp = 0.1


# Create vectors to record voltage and time
voltage = h.Vector()
time = h.Vector()


# Record membrane voltage
voltage.record(soma(0.5)._ref_v)

# Record simulation time
time.record(h._ref_t)


# Set the initial membrane voltage
h.finitialize(-65)


# Set the simulation duration
h.tstop = 100


# Run the simulation
h.run()


# Convert NEURON vectors to Python lists
voltage_data = list(voltage)
time_data = list(time)


# Find maximum and minimum voltage
max_voltage = max(voltage_data)
min_voltage = min(voltage_data)

max_index = voltage_data.index(max_voltage)
min_index = voltage_data.index(min_voltage)

max_time = time_data[max_index]
min_time = time_data[min_index]


# Print simulation results
print("Simulation completed successfully!")

print(f"Maximum voltage: {max_voltage:.3f} mV")
print(f"Maximum voltage occurs at: {max_time:.3f} ms")

print(f"Minimum voltage: {min_voltage:.3f} mV")
print(f"Minimum voltage occurs at: {min_time:.3f} ms")


# Create the plot
plt.figure(figsize=(10, 6))

plt.plot(
    time_data,
    voltage_data,
    label="Membrane Voltage"
)


# Mark maximum voltage
plt.scatter(
    max_time,
    max_voltage,
    label=f"Maximum = {max_voltage:.2f} mV"
)


# Mark minimum voltage
plt.scatter(
    min_time,
    min_voltage,
    label=f"Minimum = {min_voltage:.2f} mV"
)


# Add labels
plt.xlabel("Time (ms)")
plt.ylabel("Membrane Voltage (mV)")

plt.title("Classical Hodgkin-Huxley Action Potential")


# Add grid
plt.grid(True)


# Add legend
plt.legend()


# Display the plot
plt.show()