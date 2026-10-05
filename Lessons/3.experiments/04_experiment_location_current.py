# Experiment 4: Location of Current Injection

from modelneuron import *
import matplotlib.pyplot as plt

locations = [

    ("Soma", soma),

    ("Dendrite", dend),

    ("Axon", axon)

]

plt.figure(figsize=(10,6))

for name, section in locations: # FOR WHEN YOU HAVE 2 ITEM IN EACH ELEMENT

    time, voltage = run_simulation(

    current=0.30,

    duration=20,

    section=section
    )

    plt.plot(

        time,

        voltage,

        label=name

    )


plt.xlabel("Time (ms)")

plt.ylabel("Voltage (mV)")

plt.title("Effect of Current Injection Location")

plt.grid(True)

plt.legend()

plt.show()



# BUILD ANOTHER PLOT WITH MORE CURRENTS 


plt.figure(figsize=(15,5))

locations = [

    ("Soma", soma),

    ("Dendrite", dend),

    ("Axon", axon)

]

currents = [

    0.05,
    0.10,
    0.15,
    0.20,
    0.25,
    0.30,
    0.40,
    0.50

]

for i, (name, section) in enumerate(locations):

    plt.subplot(1,3,i+1)

    for current in currents:

        time, voltage = run_simulation(
            current,
            20,
            section
        )

        plt.plot(
            time,
            voltage,
            label=f"{current:.2f} nA"
        )

    plt.title(name)

    plt.xlabel("Time (ms)")

    if i == 0:
        plt.ylabel("Voltage (mV)")

    plt.grid(True)

    plt.legend(fontsize=7)

plt.tight_layout()

plt.show()


# CODE CHOOSING CURRENT = 0.30Na BUT 3 SUBPLOTS FOR BETTER COMPARISON
# No for loops to understand better the previous ones

current = 0.30
duration = 20


time_soma, voltage_soma = run_simulation(
    current,
    duration,
    soma,
    v_init=-65
)



time_dend, voltage_dend = run_simulation(
    current,
    duration,
    dend,
    v_init=-65
)

time_axon, voltage_axon = run_simulation(
    current,
    duration,
    axon,
    v_init=-65
)


# ============================================================
# Find maximum voltage
# ============================================================

max_soma = max(voltage_soma)
max_dend = max(voltage_dend)
max_axon = max(voltage_axon)


# ============================================================
# Find index of maximum voltage
# ============================================================

max_soma_index = voltage_soma.index(max_soma)

max_dend_index = voltage_dend.index(max_dend)

max_axon_index = voltage_axon.index(max_axon)


# ============================================================
# Find time of maximum voltage
# ============================================================

max_soma_time = time_soma[max_soma_index]

max_dend_time = time_dend[max_dend_index]

max_axon_time = time_axon[max_axon_index]

# ------------------------------------------------------------
# Create figure
# ------------------------------------------------------------

plt.figure(figsize=(15,5))

# ============================================================
# SOMA
# ============================================================

plt.subplot(1,3,1)          # 1 row, 3 columns, first graph

plt.plot(
    time_soma,
    voltage_soma
)

plt.scatter(
    max_soma_time,
    max_soma,
    s=50
)

plt.text(
    max_soma_time,
    max_soma,
    f"{max_soma:.1f} mV"
)

plt.title("Current injected into Soma")

plt.xlabel("Time (ms)")

plt.ylabel("Voltage (mV)")

plt.grid(True)

# ============================================================
# DENDRITE
# ============================================================

plt.subplot(1,3,2)          # Second graph

plt.plot(
    time_dend,
    voltage_dend
)

plt.scatter(
    max_dend_time,
    max_dend,
    s=50
)

plt.text(
    max_dend_time,
    max_dend,
    f"{max_dend:.1f} mV"
)



plt.title("Current injected into Dendrite")

plt.xlabel("Time (ms)")

plt.ylabel("Voltage (mV)")

plt.grid(True)

# ============================================================
# AXON
# ============================================================

plt.subplot(1,3,3)          # Third graph

plt.plot(
    time_axon,
    voltage_axon
)

plt.scatter(
    max_axon_time,
    max_axon,
    s=50
)

plt.text(
    max_axon_time,
    max_axon,
    f"{max_axon:.1f} mV"
)

plt.title("Current injected into Axon")

plt.xlabel("Time (ms)")

plt.ylabel("Voltage (mV)")

plt.grid(True)

# ------------------------------------------------------------
# Improve spacing between the three plots
# ------------------------------------------------------------

plt.tight_layout()

# ------------------------------------------------------------
# Display the figure
# ------------------------------------------------------------

plt.show()

print("\nPeak voltages")

print(
    f"Soma:      {max_soma:.2f} mV at {max_soma_time:.2f} ms"
)

print(
    f"Dendrite:  {max_dend:.2f} mV at {max_dend_time:.2f} ms"
)

print(
    f"Axon:      {max_axon:.2f} mV at {max_axon_time:.2f} ms"
)