import matplotlib.pyplot as plt
import numpy as np

# Create a figure and an axis
fig, ax = plt.subplots()

# Define the projection plane as a rectangle
plane = plt.Rectangle((0, 0), 2, 1, fill=True, color='lightblue', edgecolor='blue', alpha=0.5)

# Add the projection plane to the axis
ax.add_patch(plane)

# Add arrows to represent the direction of projection
ax.arrow(1, 1.5, 0, -0.4, head_width=0.1, head_length=0.1, fc='black', ec='black')
ax.arrow(1, -0.5, 0, 0.4, head_width=0.1, head_length=0.1, fc='black', ec='black')

# Set the axis limits and labels
ax.set_xlim(-1, 3)
ax.set_ylim(-1, 2)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Projection Plane Test')

# Show the plot
plt.show()
