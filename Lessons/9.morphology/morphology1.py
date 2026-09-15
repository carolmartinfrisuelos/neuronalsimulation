# learn SWC file .swc
# it contains:
# type
# x
# y
# z
# radius
# parent

# load it with NEURON's Import3d tools
# learn how to load a real neuron
"""
SWC files (.swc)

| Column | Meaning                         | Example |
| ------ | ------------------------------- | ------: |
| ID     | unique point number             |       2 |
| TYPE   | what neuronal structure it is   |       3 |
| X      | x coordinate                    |     5.0 |
| Y      | y coordinate                    |     0.0 |
| Z      | z coordinate                    |     0.0 |
| Radius | radius at that point            |     2.0 |
| Parent | ID of the previous/parent point |       1 |

Meaning of Type:

1 = soma
2 = axon
3 = basal dendrite
4 = apical dendrite
5 = fork point
6 = end point
7 = custom

Parent Example:

imagine: 
Point 1 = soma
Point 2 = dendrite
Point 3 = dendrite
Point 4 = dendrite

if parent is this:
ID    parent

1       -1
2        1
3        2
4        3

then the structure is:
        1
        │
        2
        │
        3
        │
        4

and if the parent is this:
1       -1
2        1
3        2
4        2

the strutcure will look like this:

        1
        │
        2
       / \
      3   4

Neuron Morphology Databases: https://neuromorpho.org/

Search For:

- dopaminergic neurons
- substantia nigra
- VTA
- hippocampal neurons
- cortical pyramidal neurons
- motor neurons
- mouse neurons
- rat neurons
- human neurons

To begin we will use examples: dopaminergic neurons from the substantia nigra or ventral tegmental area

different files are like:
neuron.asc
neuron.hoc
neuron.swc
---> save swc. in same folder

NEURON has tools specifically to convert morphology files into NEURON sections

SWC
 ↓
Import3d_SWC_read
 ↓
Import3d_GUI
 ↓
NEURON Sections

"""

from neuron import h

h.load_file("stdrun.hoc")
h.load_file("import3d.hoc") # NEED to load Import3D tools

#=====================================================
# 1. Read SWC file
#=====================================================

# create an object capable of reading SWC file
morphology = h.Import3d_SWC_read() 
# read this particular SWC file
morphology.input("lessons/9.morphology/KW20180701_Pair2_pre.CNG.swc")

#=====================================================
# 2. Convert morphology into NEURON sections
#=====================================================


# Create Sections from SWC points
cell = h.Import3d_GUI(morphology, 0)
# Actually create the NEURON sections corresponding to this morphology
cell.instantiate(None)

#=====================================================
# 3. Show that NEURON created sections (inspect the sections)
#=====================================================

h.define_shape() # TO VISUALIZE 

sections = list(h.allsec())
print("Number of sections:", len(sections))


for section in h.allsec():
    print(section)


for section in sections:
    print(
        section,
        "L =", section.L,
        "diam =", section.diam,
        "nseg =", section.nseg
    )


h.topology() # It kind off draws in the commnad the Neuron

#=====================================================
# 4. How to visualize 
#=====================================================
shape = h.PlotShape()
shape.show(0)
input("Press Enter to close...") # for the Python Image not to close right away