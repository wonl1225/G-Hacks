import matplotlib.pyplot as plt

import numpy as np


p1 = np.array([-1642065.46956152, -3665023.83659307, 4939794.32236649])
p2 = np.array([-1642342.59895136, -3664684.65195924, 4939960.26825631])
p3 = np.array([-1642055.3368, -3665019.3469, 4939795.45006649])


offset = p1

pts = np.array([p1 - offset, p2 - offset, p3 - offset, p1 - offset])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')


ax.plot(pts[:,0], pts[:,1], pts[:,2], linewidth=1, marker='o', markerfacecolor='red', markersize=8)


offsets = [

    (-10, -10, 0),  # Point 1: Move left and back

    (20, 20, 10),   # Point 2: Move right and up

    (20, -20, 10)   # Point 3: Move right and down (away from P1)

]

labels = ['D', 'P', 'E']

for i, txt in enumerate(labels):
    dx, dy, dz = offsets[i]
    # The most basic version: Coordinates + The Text
    ax.text(pts[i,0] + dx, pts[i,1] + dy, pts[i,2] + dz, txt)


ax.set_xlabel('X Offset (m)')
ax.set_ylabel('Y Offset (m)')
ax.set_zlabel('Z Offset (m)')
ax.set_title('Triangulation of Point E')



max_range = np.array([pts[:,0].max()-pts[:,0].min(),

                      pts[:,1].max()-pts[:,1].min(),

                      pts[:,2].max()-pts[:,2].min()]).max() / 2.0

mid_x, mid_y, mid_z = (pts[:-1,:].mean(axis=0))

ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

plt.savefig('cartesian_triangle.png')
plt.show()

