import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define the vertices of the cube
vertices = np.array([[0, 0, 0], [0, 1, 0], [1, 1, 0], [1, 0, 0],
                     [0, 0, 1], [0, 1, 1], [1, 1, 1], [1, 0, 1]])

# Define the faces of the cube using the vertices
faces = [[vertices[0], vertices[1], vertices[2], vertices[3]],
         [vertices[4], vertices[5], vertices[6], vertices[7]],
         [vertices[0], vertices[1], vertices[5], vertices[4]],
         [vertices[2], vertices[3], vertices[7], vertices[6]],
         [vertices[1], vertices[2], vertices[6], vertices[5]],
         [vertices[4], vertices[7], vertices[3], vertices[0]]]

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Add the cube to the plot
ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

# Define and add projection planes
plane_size = 2
for axis in ['x', 'y', 'z']:
    plane = np.zeros((4, 3))
    if axis == 'x':
        plane[:, 0] = 1
        plane[:, 1] = [0, 0, plane_size, plane_size]
        plane[:, 2] = [0, plane_size, plane_size, 0]
    elif axis == 'y':
        plane[:, 1] = 1
        plane[:, 0] = [0, 0, plane_size, plane_size]
        plane[:, 2] = [0, plane_size, plane_size, 0]
    elif axis == 'z':
        plane[:, 2] = 1
        plane[:, 0] = [0, 0, plane_size, plane_size]
        plane[:, 1] = [0, plane_size, plane_size, 0]
    ax.add_collection3d(Poly3DCollection([plane], facecolors='blue', linewidths=1, edgecolors='b', alpha=0.1))

# Set the axes limits and labels
ax.set_xlim([0, 2])
ax.set_ylim([0, 2])
ax.set_zlim([0, 2])
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Show the plot
plt.show()
