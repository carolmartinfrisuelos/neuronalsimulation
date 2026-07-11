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

**Real neuron**
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
- Neuron divide into smaller pieces called compartments, for example:

```python
[D]-[D]-[S]-[A]-[A]-[A]
```

Each compartment with its own: length, diameter, membrane voltage, ion channels, capacitance, resistance
