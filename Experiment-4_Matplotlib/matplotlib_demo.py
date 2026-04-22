# Experiment 4: Matplotlib
# Aim: Plot a simple graph

import matplotlib.pyplot as plt

# Data points
x = [1, 2, 3]
y = [10, 20, 30]

# Plot graph
plt.plot(x, y)

# Add labels and title
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Show graph
plt.show()