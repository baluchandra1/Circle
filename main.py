import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis
fig, ax = plt.subplots()
plt.axhline(y = 0, color = 'k', linestyle = '-')
plt.axvline(x = 0, color = 'k', linestyle = '-')

# Define the center and radius of the circle
center = (0, 0)
radius = 1

# Create an array of angles from 0 to 2*pi
theta = np.linspace(0, 2*np.pi, 100)

# Parametric equations to define the circle
x = center[0] + radius * np.cos(theta)
y = center[1] + radius * np.sin(theta)
print(x,y)
# Plot the circle
ax.plot(x, y, label='Circle')

# Set aspect ratio to be equal, so the circle isn't distorted
ax.set_aspect('equal', adjustable='box')

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('')

# Display the legend
ax.legend()
ax.grid()
# Show the plot
plt.show()
