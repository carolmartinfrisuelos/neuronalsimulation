# ============================================================
# VISUALIZING A NEURON MORPHOLOGY FROM AN SWC FILE
# ============================================================

# ------------------------------------------------------------
# 1. IMPORT LIBRARIES
# ------------------------------------------------------------

# Path allows us to work with file paths safely.
from pathlib import Path

# Matplotlib is the library we will use to visualize the neuron.
import matplotlib.pyplot as plt


# ============================================================
# 2. FIND THE SWC FILE
# ============================================================

# __file__ = the location of this Python script.
#
# Path(__file__).parent = the folder where this script is.
#
# This is useful because we don't have to write the entire
# Windows path manually.
folder = Path(__file__).parent

# Our SWC file is in the same folder as this Python script.
swc_file = folder / "KW20180701_Pair2_pre.CNG.swc"


# ============================================================
# 3. READ THE SWC FILE
# ============================================================

# We create an empty list.
#
# Each element of this list will contain information about
# one point in the neuronal morphology.
points = []


# Open the SWC file.
with open(swc_file, "r") as file:

    # Read the file one line at a time.
    for line in file:

        # ----------------------------------------------------
        # Ignore comments
        # ----------------------------------------------------
        #
        # SWC files can contain lines beginning with "#".
        # These lines contain information/comments, not neurons.
        if line.startswith("#"):
            continue

        # Ignore empty lines.
        if not line.strip():
            continue


        # ----------------------------------------------------
        # Split the line into its 7 SWC columns
        # ----------------------------------------------------
        #
        # SWC format:
        #
        # ID  TYPE  X  Y  Z  RADIUS  PARENT
        #
        data = line.split()


        # ----------------------------------------------------
        # Extract each column
        # ----------------------------------------------------

        # Unique identification number of this point.
        point_id = int(data[0])

        # Type tells us what kind of structure this point
        # belongs to.
        #
        # Common SWC types:
        #
        # 1 = soma
        # 2 = axon
        # 3 = basal dendrite
        # 4 = apical dendrite
        point_type = int(data[1])

        # Spatial coordinates of this point.
        x = float(data[2])
        y = float(data[3])
        z = float(data[4])

        # Radius of the neuronal structure at this point.
        radius = float(data[5])

        # ID of the point that comes immediately before this one.
        #
        # This is what allows us to reconstruct the branches.
        #
        # If parent = -1, this point is the root of the tree.
        parent = int(data[6])


        # ----------------------------------------------------
        # Store all this information
        # ----------------------------------------------------

        points.append(
            {
                "id": point_id,
                "type": point_type,
                "x": x,
                "y": y,
                "z": z,
                "radius": radius,
                "parent": parent
            }
        )


# ============================================================
# 4. CHECK THAT THE FILE WAS READ
# ============================================================

print("SWC file:", swc_file)

print("Number of points:", len(points))

print("\nFirst 5 points:")

for point in points[:5]:
    print(point)


# ============================================================
# 5. CREATE THE FIGURE
# ============================================================

# Create a Matplotlib figure.
#
# figsize controls the size of the window/image.
fig, ax = plt.subplots(figsize=(12, 10))


# ============================================================
# 6. RECONSTRUCT THE NEURON
# ============================================================

# We now need to connect each point with its PARENT.
#
# Remember:
#
# SWC:
#
# point 1
#    |
# point 2
#    |
# point 3
#
# If point 3 has parent = 2,
# we draw a line between point 3 and point 2.


# Create a dictionary that allows us to find a point quickly
# using its ID.
point_by_id = {}

for point in points:
    point_by_id[point["id"]] = point


# Now go through every point.
for point in points:

    # Get the ID of its parent.
    parent_id = point["parent"]


    # The root point has parent = -1.
    #
    # There is therefore no line to draw for the root.
    if parent_id == -1:
        continue


    # Find the parent point.
    parent = point_by_id[parent_id]


    # --------------------------------------------------------
    # Draw a line from the parent to the current point
    # --------------------------------------------------------

    ax.plot(
        [parent["x"], point["x"]],
        [parent["y"], point["y"]],
        linewidth=0.8
    )


# ============================================================
# 7. LABEL THE GRAPH
# ============================================================

ax.set_title(
    "Neuron morphology from SWC file",
    fontsize=16
)

ax.set_xlabel("X coordinate (µm)")
ax.set_ylabel("Y coordinate (µm)")


# ------------------------------------------------------------
# Equal aspect ratio
# ------------------------------------------------------------
#
# This is important for morphology.
#
# Without this, Matplotlib might stretch the neuron vertically
# or horizontally.
#
# "equal" means:
#
# 1 µm in X = 1 µm in Y
#
ax.set_aspect("equal")


# Add a grid to make the coordinates easier to understand.
ax.grid(True)


# ============================================================
# 8. SHOW THE NEURON
# ============================================================

# Display the Matplotlib window.
#
# This window will allow you to:
#
# - zoom
# - move around
# - inspect the morphology
# - save the figure
plt.show()