import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
initial_state = [1, 1, 1]

# Time span for the integration
t_span = [0, 50]
# Time points at which the solution is to be stored
t_eval = np.linspace(t_span[0], t_span[1], 10000)

# Solve the Lorenz system
solution = solve_ivp(lorenz, t_span, initial_state, args=(sigma, rho, beta), t_eval=t_eval)

# Extract the solution for x, y, and z
x, y, z = solution.y

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the Lorenz attractor
ax.plot(x, y, z, lw=0.5)

# Set axis labels
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

# Set the title
ax.set_title('Lorenz Attractor')

# Show the plot
plt.show()