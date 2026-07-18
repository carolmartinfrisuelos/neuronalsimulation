# Lesson 1 Notes

**Properties that determine how membrane voltage changes over time:**
- membrane
- ion channels
- electrical resistance
- capacitance
- intracellular fluid
- extracellular fluid

**What can change this properties**
- injected current
- synaptic input
- electrical stimulation
- drugs
- different ion channels

## What is NEURON?

NEURON is a software designed specifically to simulate neurons.

Instead of experimenting on a real neuron, we solve mathematical equations that describe its electrical behavior.

The output is usually the membrane voltage over time.

Python will give the instructions to NEURON.

Examples:

- To inject 0.1 nanoamperes.

```python
stim.amp = 0.1
```

- To run the experiment:

```python
h.continuerun(500)
```

## Types of Neuron Models

**Integrate-and-fire:** simple,fast,good for large networks

**Hodgkin–Huxley:** detailed ion channels biologically realistic, computationally expensive, classic model in NEURON

**Multi-compartment models:** divide a neuron into many connected pieces, they produce realistic dendrites and axons

## Structure Neuron

- **Real neuron**
```python
          Dendrites
          /\
         /  \
        /    \
         Soma
          │
          │
         Axon
```
- Neuron divide into smaller pieces called compartments, producing realistic dendrites and axons, for example:

```python
[D]-[D]-[S]-[A]-[A]-[A]
```

Each compartment with its own: length, diameter, membrane voltage, ion channels, capacitance and resistance.

## Section
- It is a continuous unbranched cable (directly analogous to an unbranched neurite)
- Sections can be connected together to form branched trees, and are endowed with properties that can vary continuously with position along their lengths.
- Sections let investigators represent neuronal anatomy without having to wrestle with the cable equation. 

## Numerical Integration Methods
- Default: **Implicit Euler**: robust stability and first order accuracy in time (sufficient for most applications).
- **Crank-Nicolson method**: secondorder accuracy, more computational cost. Prone to numerical osciallations if dt is too long, voltage clamps are present or system states are described by algebraic equations. 
- Use of adaptive integration methods:actual method is either IDA (Hindmarsh and Taylor, 1999) or CVODES (Hindmarsh and Serban, 2002)

## Spatial and Temporal Discretization
- Each section own discretization parameter **nseg**; governsnumber of interal points at which the discretized form of the cable equation is integrated and can be changed after the anatomical and biophysical properties of the model.
- Spatially non-uniform parameters and variables are described in terms of normalized distance from one end of the section

## Graphical User Interface
Powerful to combine hoc programming and the GUI. Model tools:
- Channel Builder: makes it easy to specify voltage- and ligand-gated ion channels in terms of ODEs (HH-style, including Borg-Graham formulation) and/or kinetic schemes
- CellBuilder
- Import3D tool
- Linear Circuit Builder
- Network Builder

Model analysis and optimization:
- ModelView tool
- Impedance tools
- Multiple Run Fitter 

## User-extendable library of biophysical mechanisms
Model descriptions in NMODL: simple syntax to express kinetic schemes and algebraic/differential equations
Add volatge- and ligand-gates ion channels, diffusion, buffering, active transport...

## Workflow we will use

```python
Python

↓

Create neuron

↓

Insert ion channels

↓

Inject current

↓

NEURON solves equations

↓

Voltage changes

↓

Record voltage

↓

Display graph
```

## History of the NEURON simulator

Started around the 1980s by Michael Hines and John W.Moore at Duke University. 

One great idea was to automatically subdivide neurons into compartments (sections), getting rid of the manually tracking spatial grid math. 

Around 1990s-2000s, Michael Hines and Ted Carnevale refined the software at Yale University. 

**The HOC and NMODL:**
- HOC: a legacy high-level interpreter to control simulations
- NMODL: a domain-specific lamguage that allowed researchers to write and compile custom Hodkin-Huxley or Markov-type ion channel models

Around 2010s there was a scale up and the integration of Python
- The introduction of a robust Python interface, allowing NEURON to connect with other data analysis and network-building tools (ex: NetPyNE)
- When network models included millions of detailed cells, NEURON adopted MPI protocol to run on supercomputers. 

Around the 2020s 
- CoreNEURON and New Backends: To handle higly detailed models. CoreNEURON is an optimized compute engine capable of leveraging modern multi-core CPUs and GPUs. 
- Open Source and Sustainability:  Today, NEURON is heavily utilized for large-scale projects like the Blue Brain Project and the broader computational science community.The codebase remains actively maintained at Yale´s NEURON Portal. 


## The Hodgkin-Huxley model

## References:

- [NEURON Documentation – What is NEURON?](https://www.neuronsimulator.org/en/latest/guide/what_is_neuron.html)
- [Official NEURON Documentation](https://www.neuronsimulator.org/en/latest/)
- [Python Documentation](https://docs.python.org/3/)