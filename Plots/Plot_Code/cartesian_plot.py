import matplotlib.pyplot as plt

A = {"name": "A", "X": -1641893.07187132, "Y": -3664917.00956553, "Z":  4939937.44701297}

points = {
    "B": (-1641876.08620876, -3665020.06836137, 4939862.33876146),
    "C": (-1641950.82390876, -3665089.36276137, 4939785.8960614605),
    "D": (-1642065.46956152, -3665023.83659307, 4939794.32236649),
    "E": (-1642055.3368, -3665019.3469, 4939795.45006649),
    "G": (-1642063.0380049, -3664974.06357916, 4939844.188878341),
}

dxyz = {}
for name, (x, y, z) in points.items():
    dxyz[name] = (x - A["X"], y - A["Y"], z - A["Z"])

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(0, 0, 0, color='red', s=100)

for name, (dx, dy, dz) in dxyz.items():
    ax.scatter(dx, dy, dz)

ax.set_xlabel('dX (m)')
ax.set_ylabel('dY (m)')
ax.set_zlabel('dZ (m)')
ax.set_title('Cartesian coordinate relative to A)')

ax.axis('equal')
plt.savefig('cart_plot.png')
plt.show()