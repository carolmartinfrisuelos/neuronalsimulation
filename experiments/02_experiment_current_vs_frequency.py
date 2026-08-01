# Experiment 2: Current Amplitude Vs Firing frequency

from neuron import h
import matplotlib.pyplot as plt

h.load_file("stdrun.hoc")

# Create Neuron

soma = h.Section(name="soma")
dend = h.Section(name="dend")
axon = h.Section(name="axon")

soma.L = 20
soma.diam= 20

dend.L = 300
dend.diam = 2

axon.L = 1000
axon.diam = 1

dend.connect(soma(0))
axon.connect(soma(1))

for sec in [soma, dend, axon]:

    sec.insert ("hh")

    sec.Ra = 100
    sec.cm = 1

soma.nseg = 3
dend.nseg = 11
axon.nseg = 101

stim = h.IClamp(soma(0.5))
stim.delay = 100
stim.dur = 800
h.tstop = 1000

#-----------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------


# Create FUNCTION 1: run_simulation(current)

# the purpose of this function: 
# - we input current amplitude
# - it runs NEURON
# - returns voltage and time

def run_simulation(current):

    # 1. Create current
    stim = h.IClamp(soma(0.5))
    stim.delay = 100
    stim.dur = 800
    stim.amp = current


    # 2. Time and Voltage vector and recording
    time = h.Vector() #create neurontime vector
    voltage = h.Vector() #create neuron voltage vector

    time.record(h._ref_t)
    voltage.record(soma(0.5)._ref_v)


    # 3. NEURON Parameters
    h.dt = 0.025
    h.tstop = 1000 #miliseconds

    h.finitialize(-65)
    h.run()

    return list(time), list(voltage) # return as lists in python?




# Create FUNCTION 2: spike counter()

def count_spikes(voltage):

    spikes = 0

    for i in range(1, len(voltage)):

        threshold = 0 # in other experiments it may be -20mV or so

        if voltage[i-1] < threshold and voltage[i] >= threshold:

            spikes += 1 # spikes = spikes + 1

    return spikes



# Create FUNCTION 3: find first spike time

def first_spike_time(time, voltage):

    threshold = 0

    for i in range(1, len(voltage)):

        if voltage[i-1] < threshold and voltage[i] >= threshold:

            return time[i]

    return None #if no spike is found return none



# FUNCTION 4: number_of_spikes : Raster Plot

def spike_times(time, voltage):

    threshold = 0

    spike_times = []

    for i in range(1, len(voltage)):

        if voltage[i-1] < threshold and voltage[i] >= threshold:

            spike_times.append(time[i])

    return spike_times


#--------------------------------------------------------------------------
# USE THE FUNCTIONS 
#----------------------------------------------------------------------------


# Loop over currrents

currents = [

0.00,

0.02,

0.04,

0.06,

0.08,

0.10,

0.12,

0.14,

0.16,

0.18,

0.20,

0.22,

0.24,

0.26,

0.28,

0.30,

0.35,

0.40,

0.50,

0.75,

1.00
]

# Vectors to store results

all_time = []
all_voltage = []
all_spike_times = []

frequencies = []
spike_numbers = []
first_spike_times = []

for current in currents:

    time, voltage = run_simulation(current)

    all_time.append(time)
    all_voltage.append(voltage) #save every voltage trace
    

    spikes = count_spikes(voltage) # count spikes using the function
    spike_numbers.append(spikes) # save the number of spikes
 
    frequency = spikes/(h.tstop/1000) # if h.tstop is 1000ms then frequency = spikes 
    frequencies.append(frequency)

    first_time = first_spike_time(time, voltage) #find 1st spike time using function
    first_spike_times.append(first_time) # save first spike time

    times_of_spikes = spike_times(time, voltage) # for the raster plot
    all_spike_times.append(times_of_spikes)

    print(current, spikes, frequency)


# ----------------------------------------------------------------
#PLOTS
#------------------------------------------------------------------

# 1. Plot F-I curve

plt.figure(figsize=(8,5))

plt.plot(

    currents,

    frequencies,

    marker="o"

)

plt.xlabel("Injected Current (nA)")

plt.ylabel("Firing Frequency (Hz)")

plt.title("F-I Curve")

plt.grid(True)

plt.show()


# 2. Overlay of all Voltage Traces for the Interesting Currents
plt.figure(figsize=(10,6))

interesting_currents = [

0.00,

0.20,

0.26,

0.50,

1.00
]

for i in range(len(interesting_currents)):

    plt.plot(
        all_time[i],
        all_voltage[i],
        label=f"{interesting_currents[i]} nA"
    )

plt.xlabel("Time (ms)")
plt.ylabel("Voltage (mV)")
plt.title("Voltage traces for interesting injected currents")

plt.legend()

plt.grid(True)

plt.show()

# 3. PRINT TABLE

#print header:

print()

print("-"*65)

print(f"{'Current':<12}{'Spikes':<12}{'Frequency':<15}{'First spike'}")

print("-"*65)

# print every row

for i in range(len(currents)):

    if first_spike_times[i] is None:

        spike_time = "-"

    else:

        spike_time = f"{first_spike_times[i]:.2f} ms"

    print(
        f"{currents[i]:<12}"
        f"{spike_numbers[i]:<12}"
        f"{frequencies[i]:<15.2f}"
        f"{spike_time}"
    )


# 4. RASTER PLOT

# plot of the TIME at which each action potential occurs
# Each horizontal row corresponds to one injected current
# Every small vertical line represents one action potential
# If there are many vertical lines:
# → the neuron fired many spikes.
#
# If there are no vertical lines:
# → the neuron never reached threshold.

plt.figure(figsize=(10,6))


for i in range(len(currents)): #loop through very experiment performed

    # get list containg all time spikes
    times_of_spikes = all_spike_times[i]

    # draw one vertical line for EVERY spike time
    # x = spike time (ms)
    #
    # i+0.8 and i+1.2 determine the height
    # of the small vertical line.
    #
    # Since i changes for every experiment,
    # every experiment appears on a different row

    #SYNTAX FOR vlines: plt.vlines(x, ymin, ymax, linewidth=number) 
    # vlines draws a vertical line at x for ymin to ymax
    # 0.8 and 1.2 makes every spike marker centered about each line

    plt.vlines(

        times_of_spikes,

        i + 0.8, #ymin

        i + 1.2, #ymax

        linewidth=2

    )

# Replace the y-axis numbers
# (1,2,3,4...)
# with the injected current values.
#
# Example:
#
# 1 → 0.00 nA
# 2 → 0.02 nA
# 3 → 0.04 nA

plt.yticks(

    range(1, len(currents)+1),

    [f"{current:.2f} nA" for current in currents] # SHORTCUT FOR LOOP: for current in current:

)

# Label the x-axis
plt.xlabel("Time (ms)")


# Label the y-axis
plt.ylabel("Injected Current")


# Give the figure a title
plt.title("Raster Plot of Action Potential Times")


# Add a background grid
plt.grid(True)


# Display the figure
plt.show()


# RASTER PLOT 2: only selected currents

plt.figure(figsize=(10,6))

# Only show representative currents
selected_currents = [
    0.00,
    0.10,
    0.20,
    0.22,
    0.24,
    0.30,
    0.50,
    1.00
]

# Loop through all simulated currents
for i, current in enumerate(currents):

    # Skip currents we do not want to display
    if current not in selected_currents:
        continue

    # Get the spike times corresponding to this current
    spike_times = all_spike_times[i]

    # Draw one short vertical line for each spike
    plt.vlines(
        spike_times,
        current - 0.015,
        current + 0.015,
        linewidth=2
    )

# Axis labels
plt.xlabel("Time (ms)")
plt.ylabel("Injected Current (nA)")
plt.title("Raster Plot of Action Potential Times")

# Show only the selected current values on the y-axis
plt.yticks(
    selected_currents,
    [f"{c:.2f} nA" for c in selected_currents]
)

plt.grid(True)

plt.show()