# We will check how the Action Potential frequency 
# varies depending on the duration of the current clamp

# For this experiment, we will use the just created 
# neuron model file containing the functions

from modelneuron import *
import matplotlib.pyplot as plt

currents = [
    0.00,
    0.02,
    0.04,
    0.06,
    0.08,
    0.10,
    0.12,
    0.14,
    0.16,
    0.18,
    0.20,
    0.22,
    0.24,
    0.26,
    0.28,
    0.30,
    0.35,
    0.40,
    0.50,
    0.75,
    1.00
]

durations = [

    1,

    5,

    10,

    25,

    50,

    100

]

heatmap = []

for duration in durations:

    row = []

    for current in currents:

        # Run one simulation
        
            time, voltage = run_simulation(
        
            current,
        
            duration,

            v_init=-65
        
            )
        
            # Count Spikes
            spikes = count_spikes(voltage)
        
            # Save Spike Count
            row.append(spikes)
        
            # Print results
        
            print(
        
                    f"Duration = {duration:3} ms   "
                    f"Current = {current:.2f} nA   "
                    f"Spikes = {spikes}"
        
            )
    # Finish one row
    heatmap.append(row)


# Print the MATRIX

print()

print("Spike Count Matrix")

for row in heatmap:

    print(row)


plt.figure(figsize=(8,6))


# Display the spike-count matrix as an image.
# Each cell color represents the number of spikes.

plt.imshow(

    heatmap,

    aspect="auto",

    origin="lower"

)


# Add a color scale to interpret the colors.

plt.colorbar(

    label="Number of Action Potentials"

)


# Replace x-axis positions (0,1,2,3) with current values.

plt.xticks(

    range(len(currents)),

    currents

)


# Replace y-axis positions with stimulus durations.

plt.yticks(

    range(len(durations)),

    durations

)


# Label axes.

plt.xlabel("Current Amplitude (nA)")

plt.ylabel("Stimulus Duration (ms)")


# Title.

plt.title("Spike Count Heatmap")


# Show the figure.

plt.show()
