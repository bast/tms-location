import numpy as np


def _find_closest_vertex(axis1, axis2):
    # Calculate the squared distances from the x-y axis intersection
    distances_squared = np.square(axis1) + np.square(axis2)

    # Find the index of the vertex with the minimum squared distance
    closest_vertex_index = np.argmin(distances_squared)

    return closest_vertex_index


def find_closest_vertex(mesh, position):
    if position == "vertex":
        temp_array = np.where(np.array(mesh.z) > 0)[0]
        axis1 = mesh.x
        axis2 = mesh.y
    elif position == "nasion":
        temp_array = np.where(np.array(mesh.x) > 0)[0]
        axis1 = mesh.z
        axis2 = mesh.y
    elif position == "inion":
        temp_array = np.where(np.array(mesh.x) < 0)[0]
        axis1 = mesh.z
        axis2 = mesh.y
    elif position == "left tragus":
        temp_array = np.where(np.array(mesh.y) > 0)[0]
        axis1 = mesh.z
        axis2 = mesh.x
    elif position == "right tragus":
        temp_array = np.where(np.array(mesh.y) < 0)[0]
        axis1 = mesh.z
        axis2 = mesh.x

    temp_axis1 = np.array(axis1)[temp_array]
    temp_axis2 = np.array(axis2)[temp_array]
    temp_idx = _find_closest_vertex(temp_axis1, temp_axis2)

    # map back to original index
    idx = temp_array[temp_idx]

    return idx


def find_reference_points(mesh):
    points = {}
    for position in ["vertex", "nasion", "inion", "left tragus", "right tragus"]:
        points[position] = find_closest_vertex(mesh, position)
    return points
