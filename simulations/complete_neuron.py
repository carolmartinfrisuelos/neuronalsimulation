from neuron import h

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
for sec in [soma, axon, dend]:
    sec.insert("pas")
    #pas stands for passive membrane: 
    #no sodium channels, no potassium channels, no action potentials
    #membrane behaves like a resistor and a capacitor
    sec.Ra= 100 #axial resistance in ohm-cm (Ω·cm)
    #how easily current flow inside the neurons: the smaller the easier the spread of the current
    #typical values: 50–150 Ω·cm
    sec.cm = 1 #membrane capacitance in microfarads per square centimeter (µF/cm2)
    #usually 1; increasing it means the membrane respond more slowly because it stores more electrical charge
    
    for seg in sec:
        seg.pas.g = 0.001 # g: passive conductance in siemens per square centimeter (S/cm2)
        #a larger g means leakier, allowing more ions to flow, tends to restore the membrane voltage towrd resting value quickier
        seg.pas.e = -65 # e: leak reversal potential in millivolts (mV)
        #This is the voltage the passive membrane naturally tends toward. Here we've chosen −65 mV, a common resting membrane potential for many neuron models.


print("Neuron created successfully!")