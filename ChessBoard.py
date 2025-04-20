import matplotlib.pyplot as plt
import numpy as np

# Define grid and chessboard pattern
x = np.linspace(-4, 4, 8)  # Adjusted for an 8x8 grid
y = np.linspace(-4, 4, 8)
X, Y = np.meshgrid(x, y)
extent = -4, 4, -4, 4  # Matches the chessboard grid
z1 = np.add.outer(range(8), range(8)) % 2

# Plot chessboard
plt.imshow(z1, cmap="binary_r", interpolation="nearest", extent=extent, alpha=1)

# Define mathematical function
def mathematical_overlay(x, y):
    return (1 - x / 2 + x ** 5 + y ** 6) * np.exp(-(x ** 2 + y ** 2))

# Overlay function visualization
dx, dy = 0.015, 0.05
x_fine = np.arange(-4.0, 4.0, dx)
y_fine = np.arange(-4.0, 4.0, dy)
X_fine, Y_fine = np.meshgrid(x_fine, y_fine)
z2 = mathematical_overlay(X_fine, Y_fine)

# Plot the overlay with a distinct colormap and adjusted alpha
plt.imshow(z2, cmap="viridis", alpha=0.6, interpolation="bilinear", extent=extent)

# Add title and show plot
plt.title("Chess Board with Mathematical Overlay")
plt.show()