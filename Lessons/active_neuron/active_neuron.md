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

# HODKGKIN-HUXLEY (HH)
Alan Hodgkin and Andrew Huxley discovered how neurons generate electrical signals in the squid giant axon in the 1950s.

The Hodgkin-Huxley (HH) mathematical modeldescribes how the electrical voltage across a neuron changes over time. It describes the generation and propagation of action potentials.

The membrane current is described by: 

$$
I = C_m \frac{dV}{dt} + I_{Na} + I_K + I_L
$$

As we can see it is derived from the Kirchhoff equations, since the total current of the membrane will be equal to the sum of the currents.

- $C_m$ is the membrane capacitance. The membrane stores eclectrical charge. (μF/cm2)
- $V$ is the membrane potential/ voltage; difference between inside and outside of cell (mV)
- $\frac{dV}{dt}$ is the rate of change of the membrane potential. It will describe how quickly the membrane voltage changes with time. When positive (**DEPOLARIZATION**) voltage is increasing, when negative (**REPOLARIZATION**) voltage is decreasing.
- $I$ is the external current applied to the neuron.


The ionic currents are defined using conductance-based equations based on the difference between the membrane potential $V$ and the ion's equilibrium potential $E$, together with dimensionless gating variables $(m, h, n)$:

## **Potasium Current:**

$$
I_K = \bar{g}_K n^4 (V - E_K)
$$

- $I_K$ represents current produced by potassium ions moving through potassium channels.
- $\bar{g}_K $ is the **maximum potassium conductance**, in the classic HH model is 0.036 S/cm2
- **n** represents the potassium channel activation, ranges between 0 and 1; 0≤n≤1; the higher the more potassium channels are opened. The classical HH model uses four identical activation gates, thus: n x n x n x n
- $E_K$ is the **potassium reversal potential**, in the classical HH model the value is -77mV.

## **Sodium Current:**

Depolarization
      ↓
m increases rapidly
      ↓
Sodium channels open
      ↓
Na⁺ enters
      ↓
Voltage rises
      ↓
h decreases
      ↓
Sodium channels inactivate

$$
I_{Na} = \bar{g}_{Na} m^3 h (V - E_{Na})
$$

- $I_{Na}$ is the **sodium current density**.
- $\bar{g}_{Na}$ is the **maximum sodium conductance**, it describes how easily ions can flow through the membrane. Classical HH model is:  0.12 S/cm2
- $m$ is the **sodium activation variable**. Ranges between 0≤m≤1. The closest to 1 the more activation gates are open. `**m**´ rapidly responds to depolarization. The classical HH model represents sodium activation using 3 identical activation gates. Each gate has an open probability related to m, thus, total probability: m x m x m
- $h$ is the **sodium channel inactivation**. Ranges 0≤h≤1, when decreases to 0 sodium channels become inactivated. 
- $V - E_{Na}$ is the **sodium driving force**. $E_{Na}$ is the **sodium reversal potential** which is the potential at which the net sodium current is zero. At the classic HH model this is +50mV.

## **Leak Current:**

$$
I_L = \bar{g}_L (V - E_L)
$$

- $I_L$ is the leak current, which is a passive current that represents the movement of ions through channels that are not modeled as voltage-gated sodium or potassium channel. 
- $\bar{g}_L$ is the **leak conductance**. The classical HH value is 0.0003 S/cm2.
- $E_L$ is the **leak reversal potential**, which classical HH value is -54.3mV.

## **Gating Variabls Differential Equation**
The gating variables $(n, m, h)$, which represent the probability that specific ion channels are open, follow first-order differential equations of the form:

$$
\frac{dx}{dt} = \alpha_x(V)(1-x) - \beta_x(V)x
$$

All of them vary between: 0≤m,h,n≤1

| Variable | Channel   | Function     |
| -------- | --------- | ------------ |
| (m)      | Sodium    | Activation   |
| (h)      | Sodium    | Inactivation |
| (n)      | Potassium | Activation   |

**How the Gating Variables Change**
They change with: membrane voltage and time. Alpha and Beta are voltage dependent rate constants. They determine how quickly a gate transitions between different states.

- $\alpha_x(V)$: rate at which the gate moves toward the open/activated state.
- $\beta_x(V)$: rate at which the gate moves toward the closed/inactivated state.

This variables can also be changed by the **steady-state value of the gating variable** at a particular voltage, descirbing where the gate would eventually settle if  the voltage were hel constant.Adding the **time constant** that will describe how quickly the gate approaches this steady value.

$$
\frac{dm}{dt} = \alpha_m(V)(1-m) - \beta_m(V)m
$$

$$
\frac{dh}{dt} = \alpha_h(V)(1-h) - \beta_h(V)h
$$

$$
\frac{dn}{dt} = \alpha_n(V)(1-n) - \beta_n(V)n
$$

# ACTION POTENTIAL

### Hodgkin-Huxley Model Flow

```text
External current
       │
       ▼
Membrane voltage V changes
       │
       ├─────────────┐
       │             │
       ▼             ▼
    m changes      h changes
       │             │
       └──────┬──────┘
              │
              ▼
        Sodium current
              │
              ▼
        Voltage changes
              ▲
              │
       n also changes
              │
              ▼
       Potassium current
              │
              ▼
        Voltage changes
```

- **1. RESTING STATE:** neuron is resting near membrane potential $V≈−65 mV$
- **2. BEGINNING DEPOLARIZATION:** external current is injected, and membrane voltage starts increasing $I_ext>0$
- **3. SODIUM ACTIVATION:** as voltage increases **m** increases, and sodium channels open. $I_{Na}$ becomes large, sodium enters the neuron, increasing even further the voltage, creating positive feedback.
- **4. ACTION POTENTIAL PEAK:** the membrane voltage becomes strongly depolarized and **m** is very high. However, sodium channels begin to incativate and **h** increases. At the same time potassium channels start opening; **n** increases.
- **5. REPOLARIZATION:** potassium channels start increasingly opening, potassium exits the cell and creates am outward potassium current; the same time membrane voltage decreases.
- **6. HYPERPOLARIZATION:** potassium channels may remain open for a short period and sometimes the membrane voltage can become more negative that its resting potential, which is called afterhyperpolarization.
- **7. RETURN TO REST:** The gating variables return to restig potential, after neuron will be able to generate another action potential.
