"""
DIGM 131 - Assignment 1: Procedural Scene Builder
==================================================

OBJECTIVE:
    Build a simple 3D scene in Maya using Python scripting.
    You will practice using maya.cmds to create and position geometry,
    and learn to use descriptive variable names.

REQUIREMENTS:
    1. Create a ground plane (a large, flat polygon plane).
    2. Create at least 5 objects in your scene.
    3. Use at least 2 different primitive types (e.g., cubes AND spheres,
       or cylinders AND cones, etc.).
    4. Position every object using descriptive variable names
       (e.g., house_x, tree_height -- NOT x1, h).
    5. Add comments explaining what each section of your code does.

GRADING CRITERIA:
    - [20%] Ground plane is created and scaled appropriately.
    - [30%] At least 5 objects are created using at least 2 primitive types.
    - [25%] All positions/sizes use descriptive variable names.
    - [15%] Code is commented clearly and thoroughly.
    - [10%] Scene is visually coherent (objects are placed intentionally,
            not overlapping randomly).

TIPS:
    - Run this script from Maya's Script Editor (Python tab).
    - Use maya.cmds.polyCube(), maya.cmds.polySphere(), maya.cmds.polyCylinder(),
      maya.cmds.polyCone(), maya.cmds.polyPlane(), etc.
    - Use maya.cmds.move(x, y, z, objectName) to position objects.
    - Use maya.cmds.scale(x, y, z, objectName) to resize objects.
    - Use maya.cmds.rename(oldName, newName) to give objects meaningful names.
"""

import maya.cmds as cmds

# ---------------------------------------------------------------------------
# Clear the scene so we start fresh each time the script runs.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# ---------------------------------------------------------------------------
# Ground Plane
# ---------------------------------------------------------------------------
# Descriptive variables for the ground plane dimensions and position.
ground_width = 50
ground_depth = 50
ground_y_position = 0

ground = cmds.polyPlane(
    name="ground_plane",
    width=ground_width,
    height=ground_depth,
    subdivisionsX=1,
    subdivisionsY=1,
)[0]
cmds.move(0, ground_y_position, 0, ground)

# ---------------------------------------------------------------------------
# Example Object 1 -- a simple building (cube)
# This is provided as an example. Study it, then add your own objects below.
# ---------------------------------------------------------------------------
building_width = 4
building_height = 6
building_depth = 4
building_x = -8
building_z = 5

building = cmds.polyCube(
    name="building_01",
    width=building_width,
    height=building_height,
    depth=building_depth,
)[0]
# Raise the building so its base sits on the ground plane.
cmds.move(building_x, building_height / 2.0, building_z, building)

# ---------------------------------------------------------------------------
# Create a second object using a DIFFERENT primitive type than the cube above.
# Remember to:
#   - Use descriptive variable names for size and position.
#   - Name the object meaningfully with the 'name' parameter or cmds.rename().
#   - Position it so it sits on the ground (not floating or buried).

# Object 2: Tree Trunk (cylinder)
trunk_height = 5
trunk_radius = 0.5
tree_x = 5
tree_z = 6

tree_trunk = cmds.polyCylinder(
    name="tree_trunk_01",
    height=trunk_height,
    radius=trunk_radius
)[0]

cmds.move(tree_x, trunk_height / 2.0, tree_z, tree_trunk)
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Object 3: Tree Leaves (a sphere)
leaves_radius = 2

tree_leaves = cmds.polySphere(
    name="tree_leaves_01",
    radius=leaves_radius
)[0]

cmds.move(tree_x, trunk_height + leaves_radius, tree_z, tree_leaves)
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Object 4: Lamp
lamp_height = 7
lamp_radius = 0.2
lamp_x = 2
lamp_z = -4

lamp_post = cmds.polyCylinder(
    name="lamp_post",
    height=lamp_height,
    radius=lamp_radius
)[0]

cmds.move(lamp_x, lamp_height / 2.0, lamp_z, lamp_post)

bulb_radius = 0.5

lamp_light = cmds.polySphere(
    name="lamp_light",
    radius=bulb_radius
)[0]

cmds.move(lamp_x, lamp_height + bulb_radius, lamp_z, lamp_light)
# ---------------------------------------------------------------------------




# ---------------------------------------------------------------------------
# Object 5: Bench
bench_width = 3
bench_height = 0.5
bench_depth = 1
bench_x = -2
bench_z = -3

bench_seat = cmds.polyCube(
    name="bench_seat",
    width=bench_width,
    height=bench_height,
    depth=bench_depth
)[0]

cmds.move(bench_x, bench_height / 2.0, bench_z, bench_seat)
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# T O D O (Optional): Add more objects to make your scene more interesting!
# Consider: trees, lamp posts, fences, vehicles, animals, etc.

# Object 7: Rock (another sphere)
rock_radius = 1.2
rock_x = 6
rock_z = -2

rock = cmds.polySphere(
    name="rock_01",
    radius=rock_radius
)[0]

cmds.move(rock_x, rock_radius, rock_z, rock)
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Frame All -- so the whole scene is visible in the viewport.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.viewFit(allObjects=True)
print("Scene built successfully!")
