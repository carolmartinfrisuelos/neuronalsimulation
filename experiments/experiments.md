# Experiment 1: Current Injection Threshold

systematically test:

0 nA
0.01 nA
0.02 nA
0.05 nA
0.1 nA
0.2 nA
0.5 nA
1.0 nA

How much current is required to trigger an action potential?

You can create a graph:

I injected vs N(AP)

This introduces you to rheobase/current threshold concepts.

# Experiment 2: Current Amplitude vs firing frequency 

Instead of only asking whether an AP happens, ask:

How does increasing current change firing frequency?

0.05 nA → ?
0.10 nA → ?
0.20 nA → ?
0.30 nA → ?
0.50 nA → ?
1.00 nA → ?

you could caluclate: f = Nspikes/T

and plot: I stimated vs frequency (f); having a basic F-I curve

# Experiment 3: Stimulus duration

we have: stim.dur = 1

try: 
1 ms
5 ms
10 ms
50 ms
100 ms

- Does a longer current injection produce more action potentials?

you can make a 2D experiment:

                 Stimulus amplitude
              low       medium       high

Duration
short         ?           ?            ?

medium        ?           ?            ?

long          ?           ?            ?

Create a spike-count heatmap

# Experiment 4 : where you inject current

change: stim = h.IClamp(soma(0.5))

- Does the location where current is injected affect whether an action potential is generated?

This leads directly toward cable theory.

# Experiment 5: Inject a current in different positions

soma(0.5) -> soma(0.1)......

- Does injecting current at different locations within a section change the response?

# Experiment 6 : Sodium conductance sweep

make it systematic:

gnabar_hh = 0.05
gnabar_hh = 0.10
gnabar_hh = 0.12
gnabar_hh = 0.20
gnabar_hh = 0.30


measure: 
Number of APs
Maximum voltage
Minimum voltage
Time to first AP
Firing frequency

then plot gNa vs firing frequency

# Experiment 7: Potassium conductance

- This is extremely important because potassium currents are responsible for much of:

repolarization
afterhyperpolarization
controlling excitability

- compare: 
Low K⁺ conductance
Normal K⁺ conductance
High K⁺ conductance

How does potassium conductance affect the shape and frequency of action potentials?

# Experiment 8: Sodium vs Potassium Balance

- Investigate gNa and gK

create a matrix :
 |           | Low K | Normal K | High K |
| --------- | ----- | -------- | ------ |
| Low Na    |       |          |        |
| Normal Na |       |          |        |
| High Na   |       |          |        |

- measure Nap or firing frequency
- check: Neuronal excitability is determined by the balance of ionic currents, not by sodium conductance alone.

# Experiment 9: Spatial Sodium Conductance

- experiment from before hh2:
- This will teach you about spatial channel distributions.

soma.gnabar_hh = 0.12
axon.gnabar_hh = 0.30
dend1.gnabar_hh = 0.05
dend2.gnabar_hh = 0.05
dend3.gnabar_hh = 0.05

case a: same everywhere
0.12
0.12
0.12
0.12
0.12

case b: high axon
0.12
0.30
0.05
0.05
0.05

case C: high dendrites
0.12
0.12
0.30
0.30
0.30

# Experiment 10: Distance-dependent propagation

soma → dend1 → dend3

dend1(0.5)
dend3(0.5)

Δt=tdend3​−tdend1​

- You can ask:

- How much does the action potential attenuate as it travels farther from the soma?

And:

- How much delay occurs?

- This is the beginning of cable theory.

# Experiment 11 : change dendrite length

dend1.L = 50
dend1.L = 100
dend1.L = 300
dend1.L = 500

- Then measure the voltage at the end.

This directly tests:

- How does dendritic length affect signal attenuation?

# Experiment 12 : change dendrite diameter 

- dend1.diam = 1
- dend1.diam = 2
- dend1.diam = 5

- Does a thicker dendrite transmit electrical signals more effectively?

This is an excellent introduction to cable theory.

# Experiment 13: Change axial resistance

- Then measure propagation.
Ra = 50
Ra = 100
Ra = 150
Ra = 300

Ra↑⇒less effective longitudinal current flow

and therefore affects how voltage spreads along the neuron.

# Experiment 14:Change membrane capacitance 

cm = 0.5
cm = 1.0
cm = 2.0

This teaches you how the membrane's electrical storage affects the speed of voltage changes.

You can investigate:

How does membrane capacitance affect the time required for the membrane to respond to a stimulus?

This is an excellent bridge between physics and neuroscience.

# Experiment 15 : Change membrane leak conductance 
- with passive mechanism: seg.pas.g

Low leak
Normal leak
High leak

seg.pas.g = 0.0001
seg.pas.g = 0.001
seg.pas.g = 0.01