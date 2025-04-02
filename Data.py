import numpy as np


def load_airfoil_coords(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    coords = []
    for line in lines:
        if line.strip() == "" or any(c.isalpha() for c in line):
            continue
        x, y = map(float, line.strip().split())
        coords.append((x, y))

    # Ensure the polygon is closed
    if coords[0] != coords[-1]:
        coords.append(coords[0])

    return np.array(coords)


def compute_area(coords):
    x = coords[:, 0]
    y = coords[:, 1]
    return 0.5 * np.sum(x[:-1] * y[1:] - x[1:] * y[:-1])


def compute_centroid_x(coords):
    x = coords[:, 0]
    y = coords[:, 1]
    A = compute_area(coords)
    cx = (1 / (6 * A)) * np.sum((x[:-1] + x[1:]) * (x[:-1] * y[1:] - x[1:] * y[:-1]))
    return cx


# Example usage
filename = 'atr72sm-il.dat'
coords = load_airfoil_coords(filename)
centroid_x = compute_centroid_x(coords)

print(f"Longitudinal centroid of airfoil (x̄): {centroid_x:.4f} (fraction of chord)")