# ACTIVE NEURON

Contrary to Passive neurons, in which a bigger current increases linearly a larger voltage respponse in the neuron, and **active neuron** is not linear anymore.

These neuron contain channels that will open and close automatically depending on voltage. This way, the neuron will have a positive feedback. 

- Example:

Current

↓

Voltage rises slightly

↓

Sodium channels open

↓

More sodium enters

↓

Voltage rises faster

↓

Even more sodium channels open

↓

ACTION POTENTIAL

- Inside the code we will change:

```python
sec.insert("pas") 
# for: 
sec.insert("hh")
```
## Action Potential in terms of equations:

Current injected
        │
        ▼
Membrane depolarizes
        │
        ▼
m increases rapidly
        │
        ▼
Sodium channels open
        │
        ▼
INa becomes large and inward
        │
        ▼
Membrane depolarizes even more
        │
        ▼
Positive feedback
        │
        ▼
Action potential
        │
        ▼
h decreases (sodium channels inactivate)
        │
        ▼
n increases (potassium channels open)
        │
        ▼
Potassium current repolarizes the membrane
        │
        ▼
Neuron returns to rest

## Hodkgkin-Huxley (hh)
Alan Hodgkin and Andrew Huxley discovered how neurons generate electrical signals in the squid giant axon in the 1950s.

The Hodgkin-Huxley (HH) mathematical modeldescribes how the electrical voltage across a neuron changes over time. It describes the generation and propagation of action potentials.

The membrane current is described by: 

$$
I = C_m \frac{dV}{dt} + I_{Na} + I_K + I_L
$$

- $C_m$ is the membrane capacitance.
- $\frac{dV}{dt}$ is the rate of change of the membrane potential.

The ionic currents are defined using conductance-based equations based on the difference between the membrane potential $V$ and the ion's equilibrium potential, together with dimensionless gating variables $(m, h, n)$:

- **Potasium Current:**

$$
I_K = \bar{g}_K n^4 (V - E_K)
$$

- **Sodium Current:**

$$
I_{Na} = \bar{g}_{Na} m^3 h (V - E_{Na})
$$

- **Leak Current:**

$$
I_L = \bar{g}_L (V - E_L)
$$

The gating variables $(n, m, h)$, which represent the probability that specific ion channels are open, follow first-order differential equations of the form:

- **Gating variable differential equation**

$$
\frac{dx}{dt} = \alpha_x(V)(1-x) - \beta_x(V)x
$$

