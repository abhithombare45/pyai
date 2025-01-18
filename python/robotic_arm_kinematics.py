import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Lengths of the links
L1, L2 = 2, 1.5

# Define the joint angles (changing over time for animation)
theta1_vals = np.linspace(0, np.pi/2, 100)
theta2_vals = np.linspace(0, -np.pi/4, 100)

# Function to calculate the end-effector position
def calculate_positions(theta1, theta2):
    x1 = L1 * np.cos(theta1)
    y1 = L1 * np.sin(theta1)
    x2 = x1 + L2 * np.cos(theta1 + theta2)
    y2 = y1 + L2 * np.sin(theta1 + theta2)
    return (0, x1, x2), (0, y1, y2)

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_aspect('equal')
line, = ax.plot([], [], 'o-', lw=2)

# Animation update function
def update(frame):
    theta1, theta2 = theta1_vals[frame], theta2_vals[frame]
    x, y = calculate_positions(theta1, theta2)
    line.set_data(x, y)
    return line,

# Create animation
ani = FuncAnimation(fig, update, frames=len(theta1_vals), blit=True)

# Display the animation
plt.show()