import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
a = 1.0
b = 0.2
c = 0.1
V0 = 1.0
Vcusp = 0.5 / (b**2)
Vmax = 1.0 / (b**4)

# Define the x range
x = np.linspace(0, a, 500)

# Define the potentials
V_sq = np.where((np.abs(x - a/2 - b) < c/2) | (np.abs(x - a/2 + b) < c/2), 0, V0)
V_parabolic = Vcusp * ((np.abs(x - a/2) - b)**2)
V_quartic = Vmax * ((x - a/2)**4 - b**2)**2

# Create the figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the potentials
ax.plot(x, V_sq, label='Square Double Well Potential')
ax.plot(x, V_parabolic, label='Parabolic Double Well Potential')
ax.plot(x, V_quartic, label='Quartic Double Well Potential')

# Set the axis labels
ax.set_xlabel('x/a')
ax.set_ylabel('Potential Energy')

# Set the title
ax.set_title('Double Well Potentials')

# Draw vertical lines to indicate the positions of the wells
ax.axvline(x=0, color='red', linestyle='-', linewidth=4)
ax.axvline(x=a, color='red', linestyle='-', linewidth=4)
ax.axvline(x=0.5 - b/a, color='gray', linestyle='--')
ax.axvline(x=0.5, color='gray', linestyle='--')
ax.axvline(x=0.5 + b/a, color='gray', linestyle='--')

# Set the y-axis limits
ax.set_ylim(bottom=0)

# Add legend
ax.legend()

# Show the plot
plt.show()
