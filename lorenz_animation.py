import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

def lorenz(t, state, sigma, rho, beta):
    x, y, z = state
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return [dx_dt, dy_dt, dz_dt]

# Lorenz system parameters
sigma = 10
rho = 28
beta = 8/3

# Initial conditions
initial_state = [2, 1, 1]

# Time span for the integration
t_span = [0, 50]
# Time points at which the solution is to be stored
t_eval = np.linspace(t_span[0], t_span[1], 10000)

# Solve the Lorenz system
solution = solve_ivp(lorenz, t_span, initial_state, args=(sigma, rho, beta), t_eval=t_eval)

# Extract the solution for x, y, and z
x, y, z = solution.y

# Function to update the plot
def update_plot(frame):
    current_index = frame * step_size
    ax.plot(x[:current_index], y[:current_index], z[:current_index], lw=0.5, color='blue')
    return ax,

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set axis labels
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

# Set the title
ax.set_title('Lorenz Attractor Animation')

# Define the number of frames and step size for the animation
num_frames = 200
step_size = len(x) // num_frames

# Create the animation
ani = FuncAnimation(fig, update_plot, frames=num_frames, blit=False, repeat=False)

# Display the animation
plt.show()
