from neuron import h

# Load standard NEURON library

h.load_file("stdrun.hoc") 

# Create the NEURON

soma = h.Section(name="soma")
dend = h.Section(name="dend")
axon = h.Section(name="axon")

# Morphology

soma.L = 20
soma.diam = 20

dend.L = 300
dend.diam = 2

axon.L = 1000
axon.diam = 1

# Connect the Neuron

dend.connect(soma(0))
axon.connect(soma(1))

# Insert Hodgkin-Huxley Channels

for sec in [soma, dend, axon]:

    sec.insert("hh")

    sec.Ra = 100

    sec.cm = 1

# Number of segments

soma.nseg = 3
dend.nseg = 11
axon.nseg = 101

# Current Clamp

stim = h.IClamp(soma(0.5))
stim.delay = 100
stim.dur = 1
stim.amp = 0.1

# Recording Vectors

time = h.Vector()
voltage = h.Vector()

time.record(h._ref_t)
voltage.record(soma(0.5)._ref_v)

# Simuation Settings

h.dt = 0.025
h.tstop = 1000

#--------------------------------------------------------
# FUNCTIONS
#--------------------------------------------------------

# Function 1: Run a Simulation
# Runs the neuron with any current and any duration

def run_simulation(current,duration, section, v_init=-65):

    stim = h.IClamp(section(0.5))
    stim.amp = current
    stim.dur = duration
    stim.delay = 100

    h.finitialize(v_init)
    h.run()

    return list(time),list(voltage)

# Function 2: Count Action Potentials
# Counts action potentials

def count_spikes(voltage):

    threshold= 0
    spikes = 0

    for i in range(1,len(voltage)):

        if voltage[i-1] < threshold and voltage[i] >= threshold:

            spikes += 1

    return spikes


# Function 3 : Find the time of the first spike
# Returns latency

def first_spike_time(time,voltage):

    threshold = 0

    for i in range(1, len(voltage)):

        if voltage[i-1] < threshold and voltage[i] >= threshold:

            return time[i]

    return None

# Function 4: Find the times of all spikes
# Returns every spike time for raster plots.

def spike_times(time, voltage):

    threshold = 0

    spikes = []

    for i in range(1, len(voltage)):

        if voltage[i-1] < threshold and voltage[i] >= threshold:

            spikes.append(time[i])

    return spikes

