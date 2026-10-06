# Computational Neuroscience with NEURON

## About this repository

This repository is a personal learning and portfolio project focused on **computational neuroscience, neuronal modelling, and simulation using Python and NEURON**.

The project started from the fundamentals of neuronal electrophysiology and progressively moves toward more realistic computational models.

The main goal is not only to learn how to run simulations, but to understand the **biology, mathematics, physics, and programming** behind neuronal behaviour.

The project currently progresses from simplified neuronal models toward working with **real reconstructed neuronal morphologies**.

---

# Main goal

The long-term goal of this project is to understand how the **structure and biophysical properties of neurons influence their electrical behaviour**, and how these processes can be represented computationally.

The learning progression is:

```text
Biological principles
        ↓
Passive membrane
        ↓
Active membrane
        ↓
Experiments with neuronal models
        ↓
Hodgkin-Huxley model
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
Real neuronal morphology
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
│   ├── 2.active_neuron/
│   ├── 3.experiments/
│   ├── 4.hh_recap/
│   ├── 5.cable_theory/
│   ├── 6.spatial_recording/
│   ├── 7.synapses/
│   ├── 8.two_neurons/
│   ├── 9.network/
│   └── 10.morphology/
│
├── .github/
│
├── .gitignore
│
└── README.md
```

The lessons are numbered according to the progression of the project.

The repository begins with basic neuronal electrophysiology, moves through active neuronal models and experiments, and gradually introduces spatial effects, synaptic communication, networks, and finally reconstructed neuronal morphology.

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

The main idea was to establish the relationship between:

```text
Injected current
      ↓
Membrane response
      ↓
Voltage over time
```

---

# 2. Active neuron — Hodgkin-Huxley model

The second stage introduced an **active neuronal membrane**.

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

The main conceptual progression was:

```text
Membrane voltage
      ↓
Voltage-dependent ion channels
      ↓
Na+ and K+ currents
      ↓
Action potential
```
Simulations

The active-neuron stage also contains several simulations used to study the behaviour of the Hodgkin-Huxley model.

These simulations were used to explore how an active neuron responds to different conditions and to connect the theoretical equations with the behaviour observed computationally.

The simulations focus on concepts such as:

Action potential generation
Sodium and potassium currents
Membrane voltage dynamics
Current injection
Changes in neuronal parameters
Differences between passive and active membrane behaviour

The simulations provided the basis for the experiments developed in Lesson 3, where the models were explored more systematically by changing parameters and comparing neuronal responses.


---

# 3. Experiments

After learning the basic passive and active neuronal models, this stage focuses on **experimentation and parameter exploration**.

The experiments are used to investigate how changing different parameters affects neuronal behaviour.

Rather than simply running a predefined simulation, the goal is to ask questions such as:

* What happens if the injected current changes?
* How does the membrane respond to different current amplitudes?
* How does changing membrane parameters affect the response?
* How do changes in Hodgkin-Huxley parameters influence action potentials?
* How does the neuronal response change when different parameters are modified?
* What can be learned by comparing different simulations?

This stage is important because it moves from:

> **"I know how to run the model."**

toward:

> **"I can use the model to investigate neuronal behaviour."**

The experiments therefore act as a bridge between learning the theoretical models and using them as computational tools.

---

# 4. Hodgkin-Huxley recap

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

This lesson provides a more structured review of the Hodgkin-Huxley model and reinforces the mathematical and biological concepts introduced previously.

---

# 5. Cable theory

Neurons are not electrically isolated points.

Dendrites and axons have physical length, diameter, membrane resistance, and internal resistance. Therefore, electrical signals change as they travel through neuronal processes.

Cable theory was introduced to understand:

* Voltage propagation through dendrites
* Signal attenuation
* Distance-dependent voltage changes
* The effect of neuronal geometry
* The relationship between membrane and axial resistance

One of the most important concepts introduced here is:

> **Neuronal geometry affects electrical signalling.**

This becomes especially important later when working with real neuronal morphologies.

The conceptual progression is:

```text
Electrical signal
      ↓
Propagation through neuronal processes
      ↓
Attenuation with distance
      ↓
Effect of geometry
```

---

# 6. Spatial recording

This stage focuses on recording voltage at different locations within a neuron.

Instead of asking only:

> What is the voltage at the soma?

the model can ask:

> What is the voltage at this particular location along the neuron?

This allows investigation of:

* Spatial voltage changes
* Dendritic attenuation
* Differences between recording locations
* Signal propagation through neuronal structures
* The relationship between distance and membrane potential

This stage connects cable theory with the later use of reconstructed neuronal morphology.

---

# 7. Synapses

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

Parameters such as:

* Synaptic weight
* Delay
* Event timing
* Reversal potential

can be modified to investigate their effects.

---

# 8. Two neurons

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

The focus is on understanding:

* Presynaptic voltage
* Event detection
* Synaptic transmission
* Postsynaptic responses
* Connections between neuronal models

This is the first step from modelling an isolated neuron toward modelling **interacting neurons**.

---

# 9. Networks

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

This moves from modelling individual neurons toward modelling **interacting neuronal systems**.

---

# 10. Morphology

The current stage of the project focuses on **real reconstructed neuronal morphology**.

Instead of creating an artificial neuron with a simple geometry such as:

```text
Soma
  |
Dendrite
```

the goal is to work with experimentally reconstructed neurons.

The current morphology work uses an **SWC reconstruction**.

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

These values describe the geometry and topology of the reconstructed neuron.

## Current objectives

The current stage is focused on learning how to:

* Find and download real neuronal morphology files
* Understand the SWC format
* Read an SWC file using Python
* Understand the `PARENT` relationship
* Reconstruct the neuronal tree
* Visualize morphology in 2D
* Visualize morphology in 3D
* Distinguish soma, axon, basal dendrites and apical dendrites
* Calculate basic morphological measurements
* Understand the difference between SWC points and NEURON sections
* Import reconstructed morphology into NEURON using `Import3D`

The current work therefore goes beyond simply looking at a neuron.

The objective is to understand how a morphology file represents a real biological structure and how that information can eventually be used in an electrical model.

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

One of the longer-term goals of this project is to connect the morphology work with the electrophysiology learned in the previous lessons.

The planned progression is:

```text
Real reconstructed morphology
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
   Passive membrane properties
          ↓
     Active ion channels
          ↓
      Synaptic inputs
          ↓
   Electrical simulation
```

This will allow the project to investigate questions such as:

* How does neuronal geometry affect voltage propagation?
* How does a dendritic synapse influence the soma?
* How does the location of a synapse change the postsynaptic response?
* How does a realistic morphology behave differently from a simplified neuron?
* How do neuronal structure and biophysical properties interact?

This is the direction in which the morphology work is developing.

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
* Hodgkin-Huxley modelling
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

The earlier stages focus on understanding fundamental neuronal electrophysiology and computational modelling.

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

The repository therefore contains structured lessons and experiments used to investigate neuronal behaviour.

The overall aim is to progressively move from **simple theoretical models** toward **realistic computational representations of neurons**.
