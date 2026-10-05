# Computational Neuroscience with NEURON

## About this repository

This repository is a personal learning and portfolio project focused on **computational neuroscience, neuronal modelling, and simulation with Python and NEURON**.

The project started from the fundamentals of neuronal electrophysiology and progressively moves toward more realistic computational models. The goal is not only to learn how to run simulations, but to understand the **biology, mathematics, physics, and programming** behind neuronal behaviour.

The current stage of the project focuses on working with **real reconstructed neuronal morphologies** and understanding how neuronal structure can be incorporated into computational models.

---

## Main goal

The long-term goal is to understand how the **structure and biophysical properties of neurons determine their electrical behaviour**, and how these processes can be represented computationally.

The learning progression is:

```text
Biological principles
        ↓
Membrane potential
        ↓
Passive neurons
        ↓
Active neurons
        ↓
Hodgkin-Huxley model
        ↓
Current injection experiments
        ↓
Cable theory
        ↓
Spatial recording
        ↓
Synapses
        ↓
Multiple neurons
        ↓
Small neural networks
        ↓
Real reconstructed neuronal morphology
        ↓
Realistic multi-compartment neurons
        ↓
Electrical simulations of reconstructed neurons
```

This is an ongoing project that is being developed progressively as I learn more about computational neuroscience.

---

# Repository structure

```text
neuronalsimulation/
│
├── lessons/
│   │
│   ├── 1.plots_voltage_time/
│   │   └── experiments/
│   │
│   ├── 2.active_neuron/
│   │   └── experiments/
│   │
│   ├── 3.hh_recap/
│   │
│   ├── 4.cable_theory/
│   │
│   ├── 5.spatial_recording/
│   │
│   ├── 6.synapses/
│   │
│   ├── 7.two_neurons/
│   │
│   ├── 8.network/
│   │
│   └── 9.morphology/
│
├── .github/
│
├── .gitignore
│
└── README.md
```

The lessons are numbered according to the approximate order in which I learned the concepts.

Experiments are kept inside the lesson where they belong rather than in a separate top-level folder. This makes it easier to understand the relationship between each experiment and the concepts it investigates.

---

# Learning progression

## 1. Plotting voltage over time — Passive neurons

The first stage focused on creating and understanding a **passive neuron**.

The main objective was to understand how a neuron's membrane potential changes when current is injected into it.

Topics explored include:

* Creating NEURON sections
* Defining neuronal geometry
* Passive membrane properties
* Leak channels
* Current injection with `IClamp`
* Recording membrane voltage
* Recording simulation time
* Plotting voltage against time with Matplotlib
* Changing parameters and observing their effects

At this stage, the neuron does not generate a full action potential. The focus is on understanding the basic electrical behaviour of the membrane.

### Experiments

Small experiments are stored inside this lesson because they directly investigate the concepts introduced here.

```text
1.plots_voltage_time/
│
├── lesson code
│
└── experiments/
    ├── ...
    └── ...
```

These experiments were used to change parameters and observe how the neuronal response changes.

---

# 2. Active neuron — Hodgkin-Huxley model

The second major stage introduced an **active neuronal membrane**.

Instead of representing the membrane only with passive leak behaviour, the model includes voltage-dependent ion channels.

The focus was understanding the biological and mathematical basis of the action potential.

Topics explored include:

* Sodium (`Na+`) currents
* Potassium (`K+`) currents
* Voltage-dependent conductances
* Membrane capacitance
* Membrane potential
* Gating variables
* Action potential generation
* Hodgkin-Huxley equations
* Threshold behaviour
* Effects of changing model parameters

This stage connected the biological description of ion channels with the mathematical equations used to model neuronal activity.

### Experiments

Experiments are stored inside this lesson because they investigate the active neuron and Hodgkin-Huxley model directly.

```text
2.active_neuron/
│
├── lesson code
│
└── experiments/
    ├── ...
    └── ...
```

The experiments explore how changing model parameters affects neuronal behaviour.

The purpose is to understand the model rather than simply reproduce a predefined result.

---

# 3. Hodgkin-Huxley recap

This stage consolidates the main concepts behind the Hodgkin-Huxley model.

The focus is on understanding the relationship between:

```text
Membrane voltage
      ↓
Ion-channel gating
      ↓
Na+ and K+ conductances
      ↓
Ionic currents
      ↓
Membrane potential changes
      ↓
Action potential
```

This lesson provides a bridge between the initial active-neuron experiments and the more spatially realistic models that follow.

---

# 4. Cable theory

Neurons are not electrically isolated points.

Dendrites and axons have physical length, diameter, membrane resistance, and internal resistance. Therefore, electrical signals change as they travel through neuronal processes.

Cable theory was introduced to understand:

* Voltage propagation through dendrites
* Signal attenuation
* Distance-dependent voltage changes
* The effect of neuronal geometry
* The relationship between membrane and axial resistance

An important concept introduced here is:

> **Neuronal geometry affects electrical signalling.**

This becomes especially important later when working with real neuronal morphologies.

---

# 5. Spatial recording

This stage focuses on recording voltage at different locations within a neuron.

Instead of asking only:

> What is the voltage at the soma?

the model can ask:

> What is the voltage at this particular location along the neuron?

This allows investigation of:

* Spatial voltage changes
* Dendritic attenuation
* Differences between recording locations
* How signals propagate through neuronal structures

This connects cable theory with the later use of reconstructed neuronal morphology.

---

# 6. Synapses

This stage introduces communication between neurons.

The main NEURON objects explored include:

* `ExpSyn`
* `NetStim`
* `NetCon`

The basic computational process is:

```text
Presynaptic event
       ↓
     NetCon
       ↓
     ExpSyn
       ↓
Postsynaptic current
       ↓
Postsynaptic voltage response
```

The goal is to understand how synaptic events can be represented computationally and how they change the membrane potential of a neuron.

Parameters such as synaptic weight, delay, timing, and reversal potential can be modified to investigate their effects.

---

# 7. Two neurons

The next stage connects two neurons computationally.

The basic structure is:

```text
Neuron A
   ↓
NetCon
   ↓
ExpSyn
   ↓
Neuron B
```

This introduces the idea that individual neuron models can become components of a larger circuit.

The focus is on:

* Presynaptic voltage
* Event detection
* Synaptic transmission
* Postsynaptic responses
* Connections between neuronal models

---

# 8. Networks

The network stage extends the previous idea to several neurons.

For example:

```text
Neuron 1
    ↓
Neuron 2
    ↓
Neuron 3
```

The goal is to understand how individual neurons and synapses can be combined to create small computational circuits.

Topics include:

* Creating multiple neurons
* Reusing functions to generate cells
* Connecting cells
* Synaptic chains
* Event propagation
* Small neural circuits

This moves from modelling an individual neuron toward modelling **interacting neuronal systems**.

---

# 9. Morphology

The current stage of the project focuses on **real reconstructed neuronal morphology**.

Instead of creating an artificial neuron such as:

```text
Soma
  |
Dendrite
```

the goal is to work with experimentally reconstructed neurons.

The first morphology file being explored is an **SWC reconstruction**.

An SWC file contains information such as:

```text
ID
TYPE
X
Y
Z
RADIUS
PARENT
```

This describes the geometry and topology of the reconstructed neuron.

### Current objectives

* Understand the SWC format
* Read an SWC file with Python
* Understand the `PARENT` relationship
* Reconstruct the neuronal tree
* Visualize morphology in 2D
* Visualize morphology in 3D
* Distinguish soma, axon, basal dendrites and apical dendrites
* Calculate basic morphological measurements
* Understand the difference between SWC points and NEURON sections
* Import reconstructed morphology into NEURON using `Import3D`

The longer-term goal is to connect the morphology with electrical modelling.

Conceptually:

```text
Real reconstructed neuron
          ↓
        SWC file
          ↓
   Python morphology analysis
          ↓
       3D structure
          ↓
     NEURON Import3D
          ↓
   NEURON Sections/Segments
          ↓
   Membrane mechanisms
          ↓
      Synapses
          ↓
 Electrical simulation
```

---

# Why morphology matters

A neuronal morphology file is more than a picture of a neuron.

It contains quantitative information about:

* Branching
* Length
* Diameter
* Spatial position
* Axon structure
* Dendritic structure
* Distances between different parts of the neuron

This matters because neuronal geometry affects electrical signalling.

For example, a synaptic input located close to the soma can produce a different response from the same input located far away on a dendrite.

Therefore, realistic neuronal morphology can be used to investigate how **structure influences function**.

---

# From morphology to electrical simulation

One of the longer-term goals of this project is to connect the morphology work with the electrophysiology learned in the earlier lessons.

The progression will be:

```text
SWC morphology
      ↓
Import into NEURON
      ↓
Realistic neuronal geometry
      ↓
Passive membrane properties
      ↓
Active ion channels
      ↓
Current injection
      ↓
Synaptic inputs
      ↓
Electrical response
```

This will allow questions such as:

* How does neuronal geometry affect voltage propagation?
* How does a dendritic synapse influence the soma?
* How does the location of a synapse change the postsynaptic response?
* How does a realistic morphology behave differently from a simplified neuron?
* How do neuronal structure and biophysical properties interact?

These are the concepts this project is working toward.

---

# Tools and technologies

The project currently uses:

* **Python**
* **NEURON**
* **Matplotlib**
* **NumPy** where appropriate
* **VS Code**
* **Git / GitHub**

The project also uses reconstructed neuronal morphology data in formats such as **SWC**.

---

# What I am learning

## Computational neuroscience

* Neuronal membrane dynamics
* Action potentials
* Ion channels
* Synaptic transmission
* Neural circuits
* Cable theory
* Neuronal morphology

## Programming

* Python fundamentals
* Functions
* Loops
* Dictionaries
* File handling
* Scientific data structures
* Matplotlib
* Data analysis

## NEURON

* Sections
* Segments
* Membrane mechanisms
* `IClamp`
* `NetCon`
* `NetStim`
* `ExpSyn`
* Multi-neuron networks
* Importing reconstructed morphology

---

# Project status

This is an **ongoing learning and portfolio project**.

The earlier lessons focus on fundamental neuronal electrophysiology and computational modelling.

The current stage focuses on reconstructed neuronal morphology and learning how real neuronal structure can be incorporated into computational models.

The next objective is to combine the morphological models with the electrophysiological concepts developed in the previous lessons.

---

# Future directions

Possible future stages include:

* More detailed analysis of reconstructed morphologies
* Quantitative comparison of different neuronal morphologies
* Realistic multi-compartment neurons
* Passive simulations using reconstructed neurons
* Active ion-channel models on reconstructed neurons
* Synaptic inputs at different dendritic locations
* Comparison between simplified and reconstructed neurons
* Small networks using realistic neuronal morphologies
* More advanced biophysical mechanisms
* Development of a small independent computational neuroscience project

---

# Learning philosophy

This repository is intended to document **understanding and progression**, not just finished code.

For each stage, the objective is to understand:

```text
What is happening biologically?
        ↓
What is the mathematical model?
        ↓
How is it represented computationally?
        ↓
What does the code do?
        ↓
What happens when parameters change?
        ↓
How does the result relate back to biology?
```

The repository therefore contains both structured lessons and small experiments used to investigate neuronal behaviour.
