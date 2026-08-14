# Firstly, to simplify the nested loops, we will only change the conductance in the soma:
# How does the Na/K balance of the soma affect excitability?

from modelneuron import *
import matplotlib.pyplot as plt

#----------------------------------------------------------------
# Define the Experimental Values
#----------------------------------------------------------------
current = 0.30
duration = 800

# Sodium conductance levels
sodium_levels = {
    "Low Na": 0.06,
    "Normal Na": 0.12,
    "High Na": 0.24
}

# Potassium conductance levels
potassium_levels = {
    "Low K": 0.018,
    "Normal K": 0.036,
    "High K": 0.072
}

# This dictionaries connect a name with a number:
# ex: sodium_level["Low Na"] => 0.06
# "Low Na" : its called a key
# the numbers 0.06... are called values

#----------------------------------------------------------------
# Nested Loops
#----------------------------------------------------------------

# We will try to follow the following loop:
# Low Na + Low K
# Low Na + Normal K
# Low Na + High K

# Normal Na + Low K
# Normal Na + Normal K
# Normal Na + High K

# High Na + Low K
# High Na + Normal K
# High Na + High K

results = []

for na_name, gNa in sodium_levels.items():

    # items() is a dictionary method: Give me both the key AND the value from the dictionary.

    row = [] # For the current sodium condition

    for k_name, gK in potassium_levels.items():

        time, voltage = run_ion_simulation(
            current,
            duration,
            gNa,
            gK
        )

        spikes = count_spikes(voltage)

        simulation_time_seconds = 1000 / 1000
        frequency = spikes / simulation_time_seconds



        row.append(frequency)

        print(
            f"{na_name:10} | "
            f"{k_name:10} | "
            f"Spikes = {spikes:3} | "
            f"Frequency = {frequency:.1f} Hz"
        )

    results.append(row)


# ------------------------------------------------------------------
# PLOT IN HEATMAP
# ------------------------------------------------------------------

# ============================================================
# HEATMAP
# ============================================================

plt.figure(figsize=(8, 6))

plt.imshow(
    results,
    origin="upper",
    aspect="auto"
)

plt.colorbar(
    label="Firing Frequency (Hz)"
)

plt.xticks(
    range(len(potassium_levels)),
    potassium_levels.keys()
)

plt.yticks(
    range(len(sodium_levels)),
    sodium_levels.keys()
)

plt.xlabel("Potassium Conductance")

plt.ylabel("Sodium Conductance")

plt.title(
    "Effect of Sodium and Potassium Conductance "
    "on Neuronal Excitability"
)

plt.show()




