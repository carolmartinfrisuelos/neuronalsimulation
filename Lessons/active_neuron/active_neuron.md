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

## Hodkgkin-Huxley (hh)
Alan Hodgkin and Andrew Huxley discovered how neurons generate electrical signals in the squid giant axon in the 1950s.

Main equation that describes how the membrane voltage changes over time:

$C_m\frac{dV}{dt}=I-\bar{g}_{Na}m^{3}h(V-E_{Na})-\bar{g}_{K}n^{4}(V-E_{K})-g_L(V-E_L)$

| Symbol    | Meaning              | Units  |
| --------- | -------------------- | ------ |
| (C_m)     | Membrane capacitance | µF/cm² |
| (V)       | Membrane voltage     | mV     |
| (t)       | Time                 | ms     |
| (I_{ext}) | Injected current     | µA/cm² |
| (I_{Na})  | Sodium current       | µA/cm² |
| (I_K)     | Potassium current    | µA/cm² |
| (I_L)     | Leak current         | µA/cm² |

**SODIUM CURRENT**
| Parameter     | Meaning                    | Units         |
| ------------- | -------------------------- | ------------- |
| (I_{Na})      | Sodium current             | µA/cm²        |
| (\bar g_{Na}) | Maximum sodium conductance | S/cm²         |
| (m)           | Sodium activation gate     | dimensionless |
| (h)           | Sodium inactivation gate   | dimensionless |
| (V)           | Membrane voltage           | mV            |
| (E_{Na})      | Sodium reversal potential  | mV            |

**POTASSIUM CURRENT**
| Parameter  | Meaning                         |
| ---------- | ------------------------------- |
| (n)        | Potassium activation gate       |
| (\bar g_K) | Maximum potassium conductance   |
| (E_K)      | Potassium equilibrium potential |

**LEAK CURRENT**
- Passove ion leakage

**CONDUCTANCE**