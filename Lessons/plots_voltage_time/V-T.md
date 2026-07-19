# PASIVE NEURON RESPONSE : VOLTAGE AND TIME PLOT


- Does the voltage change become larger?
- Is the relationship roughly linear?
- Does the neuron ever spike?

Since you're using only passive channels (pas), the neuron should not produce an action potential no matter how much current you inject. That illustrates the difference between passive and active membranes.


## Initial Parameters
- current injected: 0.1nA
- membrane capacitance: 1µF/cm^^2
- leak conductance: 0.001 S/cm^^2
- resting potential: -65mV
- IClamp: soma(0.5)


## CHANGE CURRENT (stim.amp)

**0.05nA**
- Maximum voltage: -63.321 mV at 40.700 ms
- Minimum voltage: -65.000 mV at 0.000 ms

**0.1nA**
- Maximum voltage: -61.641 mV at 41.225 ms
- Minimum voltage: -65.000 mV at 0.000 ms

**0.2nA**
- Maximum voltage: -58.283 mV at 41.950 ms
- Minimum voltage: -65.000 mV at 0.000 ms

**0.5nA**
- Maximum voltage: -48.207 mV at 43.125 ms
- Minimum voltage: -65.000 mV at 0.000 ms

## CHANGE MEMBRANE CAPACITANCE (sec.cm)

**1 µF/cm^^2**
- Maximum voltage: -63.321 mV at 40.700 ms
- Minimum voltage: -65.000 mV at 0.000 ms

**2 µF/cm^^2**
- Maximum voltage: -63.321 mV at 60.000 ms
- Minimum voltage: -65.000 mV at 0.000 ms

**10 µF/cm^^2**
- Maximum voltage: -63.328 mV at 60.000 ms
- Minimum voltage: -65.000 mV at 0.000 ms

**30 µF/cm^^2**
- Maximum voltage: -63.546 mV at 60.000 ms
- Minimum voltage: -65.000 mV at 0.000 ms

**0.01 µF/cm^^2**
- Maximum voltage: -63.321 mV at 10.675 ms
- Minimum voltage: -65.000 mV at 0.000 ms

## CHANGE THE LEAK CONDUCTANCE (seg.pas.g)
- A higher leak conductance makes the membrane "leakier." The voltage is pulled back toward the resting potential more quickly.

**0.001 S/cm^^2**
- Maximum voltage: -63.321 mV at 40.700 ms
- Minimum voltage: -65.000 mV at 0.000 ms

**0.0001 S/cm^^2**
- Maximum voltage: -54.065 mV at 60.000 ms
- Minimum voltage: -65.000 mV at 0.000 ms

**0.01 S/cm^^2**
- Maximum voltage: -64.731 mV at 13.225 ms
- Minimum voltage: -65.000 mV at 0.000 ms


## CHANGE THE RESTING POTENTIAL (seg.pas.e)

- This changes the voltage that the passive membrane naturally tends toward.

**-65mV**
- Maximum voltage: -63.321 mV at 40.700 ms
- Minimum voltage: -65.000 mV at 0.000 ms

**-70mV**
- Maximum voltage: -65.000 mV at 0.000 ms
- Minimum voltage: -70.000 mV at 88.925 ms

**-55mV**
- Maximum voltage: -53.321 mV at 40.775 ms
- Minimum voltage: -65.000 mV at 0.000 ms

## INJECT CURRENT TO DIFFERENT LOCATIONS (stim = h.IClamp(soma(0.5)))

- The response at the soma will differ because electrical signals attenuate as they travel through the neuron. 

**stim = h.IClamp(dend(0.5))**
- Maximum voltage: -63.987 mV at 40.850 ms
- Minimum voltage: -65.000 mV at 0.000 ms

**stim = h.IClamp(axon(0.5))**
- Maximum voltage: -64.929 mV at 40.075 ms
- Minimum voltage: -65.000 mV at 0.000 ms

## PLOT OF SOMA, AXON AND DENDRITE V-T
