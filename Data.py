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

    return np.array(coords)

def compute_airfoil_area(coords):
    x = coords[:, 0]
    y = coords[:, 1]
    area = 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
    return area

# Example usage
filename = 'atr72sm-il.dat'
coords = load_airfoil_coords(filename)
area = compute_airfoil_area(coords)

# Optional: convert to real area with chord length
chord_length = 3.78  # meters
true_area = area * chord_length**2

print(f"Enclosed area of airfoil (normalized): {area:.5f}")
print(f"Enclosed area with chord = {chord_length} m: {true_area:.5f} m²")