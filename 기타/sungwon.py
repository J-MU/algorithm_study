from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt
import numpy as np

u = np.array([6,3,1])
v = np.array([2,6,5])

print(u)
print(v)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.title.set_text('2019110610 SeongWon Jeong')

# x축 범위설정
ax.set_xlim(0,8)
ax.set_ylim(0,8)
ax.set_zlim(0,8)

# x,y,z 축이름설정인듯?
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# x,y,z 축 간격설정
ax.set_xticks([0,2,4,6,8])
ax.set_yticks([0,2,4,6,8])
ax.set_zticks([0,2,4,6,8])

#몰라이건 신경쓰지말고
ax.quiver(0, 0, 0, u[0], u[1], u[2], color='red', arrow_length_ratio=0.1)
ax.text(u[0], u[1], u[2], 'u', size=15)
ax.quiver(0, 0, 0, v[0], v[1], v[2], color='blue', arrow_length_ratio=0.1)
ax.text(v[0], v[1], v[2], 'v', size=15)
plt.show()