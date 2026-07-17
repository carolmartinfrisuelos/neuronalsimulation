from neuron import h

# Create one section representing the cell body
soma = h.Section(name="soma")
axon = h.Section(name="axon")

# Geometry
soma.L = 20 #length of the section with unit micrometers (µm)
soma.diam = 20 #diameter of the section with unit micrometers (µm)

# Print information
print("Section name:", soma.name())
print("Length:", soma.L, "µm")
print("Diameter:", soma.diam, "µm")
#the '.' in python mean access something that belongs to this object
#the pattern is always object.property or object.method()
#Notice the parentheses on name(). That tells you it's a method (an action), 
#whereas L and diam are properties (stored values).
print(soma.name())
print(axon.name())