# 2019110610 정성원
import numpy as np
import matplotlib.pyplot as plt

u = np.array([6,3,1])
v = np.array([2,6,5])

fig = plt.figure()
ax = fig.add_subplot(1,1,1,projection='3d')
ax.title.set_text('2019110610 SeongWon Jeong')

ax.set_xlim(0,8)
ax.set_ylim(0,8)
ax.set_zlim(0,8)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_xticks([0,2,4,6,8])
ax.set_yticks([0,2,4,6,8])
ax.set_zticks([0,2,4,6,8])

ax.quiver(0, 0, 0, u[0], u[1], u[2], color='red', arrow_length_ratio=0.1)
ax.text(u[0], u[1], u[2], 'u', size=15)
ax.quiver(0, 0, 0, v[0], v[1], v[2], color='blue', arrow_length_ratio=0.1)
ax.text(v[0], v[1], v[2], 'v', size=15)

x, y = np.meshgrid(np.arange(9), np.arange(9))
l = np.cross(u,v)

print(l)
z = (-9/30)*(x-6)+(28/30)*(y-3)+float(1)
# z=(-9)*(x-6)+(y-3)+1
ax.plot_surface(x, y, z, alpha=0.5)
ax.view_init(elev=15., azim=-120)
plt.show()