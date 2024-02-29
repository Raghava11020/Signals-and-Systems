import matplotlib.pyplot as plt
import numpy as np

# Function to plot a circle
def plot_circle(center, radius, highlight=False):
    theta = np.linspace(0, 2*np.pi, 100)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    plt.plot(x, y, label=f"Center: {center}, Radius: {radius}", linewidth=2)
    
    if highlight:
        plt.scatter(center[0], center[1], color='red', marker='o', label='Highlighted Point')

# Circle details
centers = [(2, 0), (1, 0), (3, 0), (0, 0)]
radii = [0.01, 0.1, 5, 2]

# Plot each circle
for center, radius in zip(centers, radii):
    plot_circle(center, radius, highlight=(center == (1, 0)))

# Set aspect ratio to be equal for a perfect circle display
plt.gca().set_aspect('equal', adjustable='box')

# Set axis limits
plt.xlim(-6, 6)
plt.ylim(-6, 6)

# Add labels and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Circles with Centers and Radii')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()

