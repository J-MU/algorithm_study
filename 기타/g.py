from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


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


x,y=np.meshgrid(np.arange(9),np.arange(9))
z=x*5+y
ax.plot_surface(x, y, z, cmap="brg_r")
plt.show()
print(x)
print(type(x))