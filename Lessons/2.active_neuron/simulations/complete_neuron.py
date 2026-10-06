from neuron import h
h.load_file("stdrun.hoc") #is a file that comes with NEURON defining tstop, run(), finitialize()

# Create the neuron sections
soma = h.Section(name="soma")
axon = h.Section(name="axon")
dend = h.Section(name="dendrite")

#Realistic Geometry
# Soma
soma.L = 20
soma.diam = 20
#Most mammalian neurons have soma diameter of10–40 µm

# Axon
axon.L = 1000
axon.diam = 1
#It is 1mm, many axons are much longer; 
#some motor neurons have axons over 1 meter;
#we simmulate the part we are interest in
#the typical values of the diamter is 0.2,0.5,1,2 micrometers (µm)
#a thinner axon has higher electrical resistance and slower conduction velocity, but it is more space efficient.

# Dendrite
dend.L = 300
dend.diam = 2

print(soma.name(), soma.L, soma.diam)
print(axon.name(), axon.L, axon.diam)
print(dend.name(), dend.L, dend.diam)

#Connect the sections
axon.connect(soma(1)) #attach beginning of the axon to the end of the soma
dend.connect(soma(0)) #attach dendrite to the other side of the soma 
#now neuron looks: dendrite---soma---axon

#Divide Sections into Compartments: nseg

soma.nseg = 1 #usually 1 compartment

axon.nseg = 101 #51-201 compartments for long axons, 101 is a good compromise between accuracy and speed

dend.nseg = 31 #11-51 compartments

#Why divide into sections?
#Because electricity changes continuously.
#NEURON approximates this by solving equations compartment by compartment.
#When choosing same compartment; the simulator assumes the volatage is almost uniform over the entire millimeter
#You can calculate the compartment length by :
print(axon.L / axon.nseg)

#Add passive properties to the sections

#Membrane:

#Passive Membrane
# we use a foor loop because the same operations are repeated for each section
for sec in [soma, axon, dend]:

    sec.insert("pas")
    #pas stands for passive membrane: 
    #no sodium channels, no potassium channels, no action potentials
    #membrane behaves like a resistor and a capacito
    
    sec.Ra= 100 #axial resistance in ohm-cm (Ω·cm)
    #how easily current flow inside the neurons: the smaller the easier the spread of the current
    #typical values: 50–150 Ω·cm

    sec.cm = 1 #membrane capacitance in microfarads per square centimeter (µF/cm2)
    #usually 1; increasing it means the membrane respond more slowly because it stores more electrical charge

    
    for seg in sec:
        seg.pas.g = 0.001 # g: passive conductance in siemens per square centimeter (S/cm2)
        #a larger g means leakier, allowing more ions to flow, tends to restore the membrane voltage toward resting value quickier

        seg.pas.e = -65 # e: leak reversal potential in millivolts (mV)
        #This is the voltage the passive membrane naturally tends toward. Here we've chosen −65 mV, a common resting membrane potential for many neuron models.


#Create a current clamp to inject current into the soma

stim = h.IClamp(soma(0.5))  #IClamp means current clamp: represents a laboratory electrode that injects a current
#0.5 means the middle of the some (goes from 0 to 1)
#basically we just put the electrode in the middle of the soma
    
stim.delay = 10 #delay in miliseconds (wait 10ms before injecting anything)
stim.dur = 50 #inject current for an amount of time; 50 ms
stim.amp = 0.1 #nanoamps (nA); higher the amps the larger response; 
#more than 1nA may trigger an action potential if active channel exist
    
#Create vectors to record voltage and time
v = h.Vector()
t = h.Vector()

v.record(soma(0.5)._ref_v) #record saves data continuosly; 0.5 middle of some;_ref_v is the memory location where membrane volatage is stored (a reference)
t.record(h._ref_t); # record time _ref_t is the simulation clock

#Set Initial Voltage
h.finitialize(-65) #start simmulation at -65 mV

#Decide how long to simulate
h.tstop = 100 #units in miliseconds

#Run the simulation; NEURON solves the differential equations
h.run()

#Print the results
print("Number of voltage points:", len(v))
print(len(t))

print("First 10 voltage values:")
print(v[10:])
# the first values should be around -65 because
# the simulation begins at rest

print(v[-10:])
# last values of the simulation

print("Neuron created successfully!")

#convert the NEURON vector into a normal python list so you can see inisde the vector
time = t.to_python()
voltage = v.to_python() 

print("First 10 samples")

for i in range(500):
    print(f"{time[i]:6.2f} ms    {voltage[i]:8.3f} mV")

    #the colon (:) introduces formating instructions
    #the f shows a floating-point number; a decimal number
    #.2 means 2 digits after decimal point
    #the 6 means reserve at least 6 character spaces for the number.

#Other way to display the results: 
time = t.to_python()
voltage = v.to_python()

for i in range(10):
    print("Time:", time[i], "ms")
    print("Voltage:", voltage[i], "mV")
    print("-------------------")

print(time[390:420])
print(voltage[390:420])