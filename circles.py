import matplotlib.pyplot as plt
import numpy as np

# Function to generate points on a circle
def generate_circle_points(center, radius, num_points=10):
    angles = np.linspace(0, 2 * np.pi, num_points)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    return x, y

# Circle 1: centered at (0, 0), radius 1
x1, y1 = generate_circle_points((0, 0), 1)

# Circle 2: centered at (2, 0), radius 1
x2, y2 = generate_circle_points((2, 0), 1)

# Plot both circles
plt.plot(x1, y1, label='Circle 1')
plt.plot(x2, y2, label='Circle 2')

# Styling
plt.gca().set_aspect('equal')
plt.grid(True)
plt.legend()
plt.title('Two Circles (generated points)')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-2, 4)
plt.ylim(-2, 2)

plt.show()
