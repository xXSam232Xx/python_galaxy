import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

n_stars = 30000
np.random.seed(42)

r = np.random.uniform(0.5, 10, n_stars)
theta = np.random.uniform(0, 2 * np.pi, n_stars) + r * 0.5

x = r * np.cos(theta)
y = r * np.sin(theta)
z = np.random.normal(0, 0.2, n_stars) * (10 - r)

fig = plt.figure(figsize=(9, 9), facecolor="#0f172a")
ax = fig.add_subplot(projection="3d")
ax.set_facecolor("#0f172a")

scatter = ax.scatter(x, y, z, c=r, cmap="plasma", s=0.6, alpha=0.7)

ax.set_axis_off()
ax.set_box_aspect([1, 1, 0.4])

def update(frame):
    angle = frame * 0.02
    x_rot = x * np.cos(angle) - y * np.sin(angle)
    y_rot = x * np.sin(angle) + y * np.cos(angle)
    
    ax.clear()
    ax.set_facecolor("#0f172a")
    ax.set_axis_off()
    ax.set_box_aspect([1, 1, 0.4])
    ax.scatter(x_rot, y_rot, z, c=r, cmap="plasma", s=0.6, alpha=0.7)
    return scatter,

print("Generando galaxia 3D en rotación...")
ani = FuncAnimation(fig, update, frames=300, interval=30, blit=False)

plt.tight_layout()
plt.show()
