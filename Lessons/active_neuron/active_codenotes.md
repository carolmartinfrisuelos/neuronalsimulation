
# Active Neuron Code Notes

```python
sec.insert("hh") #hh means Hodgkin-Huxley mechanism
``` 

## Most common used parameters

```python
gnabar_hh #Maximum Sodium Conductance: 0.12 S/cm²
gkbar_hh #Maximum potassium conductance: 0.036 S/cm²
gl_hh #Leak conductance: 0.0003 S/cm²
el_hh #Leak reversal potential: -54.3 mV
```

They can be modified inside this for loop:

```python
for seg in soma:
    seg.hh.gnabar = 0.12
    seg.hh.gkbar = 0.036
    seg.hh.gl = 0.0003
    seg.hh.el = -54.3
```

## Variables you can record 
| Variable     | Meaning                       | Units         |
| ------------ | ----------------------------- | ------------- |
| `_ref_v`     | Membrane voltage              | mV            |
| `_ref_ina`   | Sodium current                | mA/cm²        |
| `_ref_ik`    | Potassium current             | mA/cm²        |
| `_ref_il_hh` | Leak current                  | mA/cm²        |
| `_ref_m_hh`  | Sodium activation gate (m)    | Dimensionless |
| `_ref_h_hh`  | Sodium inactivation gate (h)  | Dimensionless |
| `_ref_n_hh`  | Potassium activation gate (n) | Dimensionless |

An example of recording will be:

```python
m = h.Vector()
m.record(soma(0.5)._ref_m_hh)
```

# MOST IMPORTANT PARAMETERS

| Symbol | Meaning | Classical HH value | NEURON parameter |
| --- | --- | ---: | --- |
| $C_m$ | Membrane capacitance | $1 \ \mu F/cm^2$ | `sec.cm` |
| $\bar{g}_{Na}$ | Maximum Na⁺ conductance | $0.12 \ S/cm^2$ | `seg.hh.gnabar` |
| $\bar{g}_K$ | Maximum K⁺ conductance | $0.036 \ S/cm^2$ | `seg.hh.gkbar` |
| $g_L$ | Leak conductance | $0.0003 \ S/cm^2$ | `seg.hh.gl` |
| $E_L$ | Leak reversal potential | $-54.3 \ mV$ | `seg.hh.el` |
| $E_{Na}$ | Na⁺ reversal potential | approximately $+50 \ mV$ | Mechanism-dependent |
| $E_K$ | K⁺ reversal potential | approximately $-77 \ mV$ | Mechanism-dependent |
| $m$ | Na⁺ activation | $0$– $1$ | `m_hh` |
| $h$ | Na⁺ inactivation | $0$– $1$ | `h_hh` |
| $n$ | K⁺ activation | $0$– $1$ | `n_hh` |