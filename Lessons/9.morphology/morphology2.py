"""

- What can we calculate with MORPHOLOGY?

total dendritic length
number of branches
number of bifurcations
maximum distance from soma
average diameter
axon length
dendritic length
surface area
volume

- Questions you can ask:

How many points?
How many soma points?
How many axon points?
How many dendrite points?
What is the maximum distance from the soma?
What is the total dendritic length?
How many branches does the neuron have?

-Main idea: How morphology affects electrical behaviour

dendrites have:

membrane resistance
membrane capacitance
axial resistance
ion channels
branching
changing diameter

geometry → physics → electrophysiology → neuroscience

To know how neurons connect you need other sources:

- Connectivity can come from other sources:

electrophysiology experiments
anatomical tracing
connectomics
synaptic datasets
published literature
experimental connectivity matrices
network models

- FUTURE WORKFLOW MAY BE: 

                REAL NEURON DATA
                       │
                       ▼
                 NeuroMorpho
                       │
                       ▼
                    SWC file
                       │
                       ▼
                3D morphology
                       │
                       ▼
              NEURON Import3D
                       │
                       ▼
             Realistic neuron
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
      membrane                  morphology
      channels                    analysis
          │                         │
          ▼                         ▼
    electrical model          branch lengths
          │                   surface area
          │                   dendritic tree
          ▼                         │
       synapses                     │
          │                         │
          └──────────┬──────────────┘
                     ▼
              ELECTRICAL RESPONSE
                     │
                     ▼
          action potentials / PSPs
                     │
                     ▼
             biological question

"""

#=================================================================================
# 3D Visulaization + Color Morphology by type + calculate morphology
#=================================================================================

# ============================================================
# LESSON: 3D VISUALIZATION AND BASIC MORPHOLOGY OF AN SWC FILE
# ============================================================
#
# Put this Python file in the SAME folder as:
#     KW20180701_Pair2_pre.CNG.swc
#
# 1. Read the SWC file.
# 2. Understand ID, TYPE, X, Y, Z, RADIUS and PARENT.
# 3. Reconstruct the tree using PARENT.
# 4. Visualize the neuron in 3D.
# 5. Color it by morphology TYPE.
# 6. Calculate basic morphology measurements.
# ============================================================

from pathlib import Path
import math
import matplotlib.pyplot as plt


# ============================================================
# 1. FIND THE SWC FILE
# ============================================================
# __file__ = location of this Python script.
# Path(__file__).parent = folder containing this script.
# "/" joins paths.

folder = Path(__file__).parent
swc_file = folder / "KW20180701_Pair2_pre.CNG.swc"

print("Reading:", swc_file)


# ============================================================
# 2. READ THE SWC FILE
# ============================================================
# SWC columns:
# ID  TYPE  X  Y  Z  RADIUS  PARENT

points = []

with open(swc_file, "r") as file:

    for line in file:

        # Ignore comments.
        if line.startswith("#"):
            continue

        # Ignore empty lines.
        if not line.strip():
            continue

        # Separate the 7 columns.
        data = line.split()

        point_id = int(data[0])
        point_type = int(data[1])

        x = float(data[2])
        y = float(data[3])
        z = float(data[4])

        radius = float(data[5])
        parent = int(data[6])

        # Store one SWC point.
        point = {
            "id": point_id,
            "type": point_type,
            "x": x,
            "y": y,
            "z": z,
            "radius": radius,
            "parent": parent
        }

        points.append(point)


# ============================================================
# 3. CHECK THE DATA
# ============================================================

print("Number of SWC points:", len(points))

print("\nFirst 5 points:")

for point in points[:5]:
    print(point)


# ============================================================
# 4. CREATE A FAST ID -> POINT LOOKUP
# ============================================================
# We need to answer questions such as:
#
# "The parent is point 180. Where is point 180?"
#
# The dictionary lets us write:
#
#     point_by_id[180]

point_by_id = {}

for point in points:
    point_by_id[point["id"]] = point


# ============================================================
# 5. DEFINE SWC TYPES
# ============================================================

type_names = {
    1: "Soma",
    2: "Axon",
    3: "Basal dendrite",
    4: "Apical dendrite"
}


# ============================================================
# 6. COUNT POINTS BY TYPE
# ============================================================

type_counts = {}

for point in points:

    point_type = point["type"]

    if point_type not in type_counts:
        type_counts[point_type] = 0

    type_counts[point_type] += 1


print("\nNumber of points by morphology type:")

for point_type, count in type_counts.items():

    name = type_names.get(point_type, f"Type {point_type}")

    print(f"{name}: {count}")


# ============================================================
# 7. CREATE THE 3D FIGURE
# ============================================================

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection="3d")


# ============================================================
# 8. RECONSTRUCT AND COLOR THE NEURON
# ============================================================
#
# The SWC gives:
#
#     CURRENT POINT -> PARENT POINT
#
# If PARENT = -1, the point is the root and has no parent.
#
# Otherwise we find the parent and draw a line from:
#
#     parent -> current point
#
# The color is chosen from the TYPE of the current point.

type_colors = {
    1: "black",
    2: "red",
    3: "blue",
    4: "green"
}

used_types = set()

for point in points:

    parent_id = point["parent"]

    # Root: there is no parent connection to draw.
    if parent_id == -1:
        continue

    # Find the parent point.
    parent = point_by_id[parent_id]

    point_type = point["type"]

    color = type_colors.get(point_type, "gray")

    used_types.add(point_type)

    # Draw one parent-child segment in 3D.
    ax.plot(
        [parent["x"], point["x"]],
        [parent["y"], point["y"]],
        [parent["z"], point["z"]],
        color=color,
        linewidth=0.8
    )


# ============================================================
# 9. CREATE A LEGEND
# ============================================================

for point_type in sorted(used_types):

    name = type_names.get(point_type, f"Type {point_type}")
    color = type_colors.get(point_type, "gray")

    ax.plot([], [], [], color=color, linewidth=2, label=name)

ax.legend()


# ============================================================
# 10. LABEL THE 3D GRAPH
# ============================================================

ax.set_title("3D neuron morphology from SWC", fontsize=16)

ax.set_xlabel("X (um)")
ax.set_ylabel("Y (um)")
ax.set_zlabel("Z (um)")

plt.show()


# ============================================================
# 11. CALCULATE TOTAL MORPHOLOGY LENGTH
# ============================================================
#
# For every point with a parent:
#
#     dx = current X - parent X
#     dy = current Y - parent Y
#     dz = current Z - parent Z
#
# 3D distance:
#
#     sqrt(dx^2 + dy^2 + dz^2)
#
# Total morphology length = sum of all parent-child distances.

total_length = 0.0

for point in points:

    parent_id = point["parent"]

    if parent_id == -1:
        continue

    parent = point_by_id[parent_id]

    dx = point["x"] - parent["x"]
    dy = point["y"] - parent["y"]
    dz = point["z"] - parent["z"]

    distance = math.sqrt(dx**2 + dy**2 + dz**2)

    total_length += distance


print("\nTotal morphology length:")
print(f"{total_length:.2f} um")


# ============================================================
# 12. CALCULATE SPATIAL EXTENT
# ============================================================
# How much physical space does the reconstruction occupy?

x_values = []
y_values = []
z_values = []

for point in points:

    x_values.append(point["x"])
    y_values.append(point["y"])
    z_values.append(point["z"])


x_size = max(x_values) - min(x_values)
y_size = max(y_values) - min(y_values)
z_size = max(z_values) - min(z_values)


print("\nSpatial extent:")
print(f"X: {x_size:.2f} um")
print(f"Y: {y_size:.2f} um")
print(f"Z: {z_size:.2f} um")


# ============================================================
# 13. FIND THE SWC ROOT
# ============================================================

root = None

for point in points:

    if point["parent"] == -1:
        root = point
        break


print("\nRoot point:")

if root is not None:
    print(root)


# ============================================================
# 14. DISTANCE FROM ROOT TO FARTHEST POINT
# ============================================================
#
# This is simply a geometric distance from the SWC root.
# It is not automatically the same thing as path distance
# along the dendritic tree.

if root is not None:

    max_distance = 0.0
    farthest_point = None

    for point in points:

        dx = point["x"] - root["x"]
        dy = point["y"] - root["y"]
        dz = point["z"] - root["z"]

        distance = math.sqrt(dx**2 + dy**2 + dz**2)

        if distance > max_distance:
            max_distance = distance
            farthest_point = point


    print("\nFarthest point from the SWC root:")
    print(f"Distance: {max_distance:.2f} um")
    print(f"Point ID: {farthest_point['id']}")


# ============================================================
# WHAT THIS LESSON MEANS
# ============================================================
#
# SWC POINTS
#     ↓
# ID + TYPE + X/Y/Z + RADIUS + PARENT
#     ↓
# PARENT relationships reconstruct the tree
#     ↓
# 3D visualization shows the physical morphology
#     ↓
# TYPE gives biological categories
#     ↓
# measurements turn morphology into quantitative data
#
# Important:
#
# SWC POINTS != NEURON SECTIONS
#
# Later, NEURON Import3D can transform this morphology into
# NEURON Sections and Segments. Then we can add membrane
# mechanisms, synapses and electrical behavior.
# ============================================================