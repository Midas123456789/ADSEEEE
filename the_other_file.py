import numpy as np
import matplotlib.pyplot as plt

# Simulated spiral-like data
theta = np.linspace(0, 4 * np.pi, 100)
r = np.linspace(25000, 39000, 100)
x = np.sin(theta) * 5 + 30  # CG [%MAC]
y = r  # mass [kg]

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor('gray')

# Plot the spiral in segments with different colors
segments = [
    ('yellow', 0, 20),
    ('cyan', 20, 40),
    ('magenta', 40, 60),
    ('blue', 60, 80),
    ('teal', 80, 100),
]
for color, start, end in segments:
    ax.plot(x[start:end], y[start:end], marker='o', color=color)

# Add mass limits
ax.axhline(39000, color='red', linewidth=2)
ax.text(31, 39000, 'MFW', color='red', va='bottom', fontsize=12, fontweight='bold')
ax.axhline(45000, color='red', linewidth=2)
ax.text(31, 45000, 'MTOW', color='red', va='bottom', fontsize=12, fontweight='bold')
ax.axhline(25000, color='red', linewidth=2)
ax.text(31, 25000, 'ZFW', color='red', va='top', fontsize=12, fontweight='bold')

# Label axes
ax.set_xlabel('CG [%MAC]')
ax.set_ylabel('mass [kg]')

# Grid and range
ax.grid(True)
ax.set_xlim(28, 34)
ax.set_ylim(25000, 46000)

# Example of adding arrows
ax.annotate('', xy=(30, 37000), xytext=(30, 35000),
            arrowprops=dict(arrowstyle='<->', color='black'))
ax.annotate('Δ mass', xy=(30.1, 36000), color='black')

# Optional circle (you can adjust position)
circle = plt.Circle((30, 25500), 1, color='red', fill=False, linewidth=3)
ax.add_patch(circle)

plt.tight_layout()
plt.show()
