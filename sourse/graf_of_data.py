# импортируем необходимые модули
import matplotlib.pyplot as plt
import numpy as np
#
# for i in ['dataXY_with_hindrance.txt']:
#     with open(i) as f:
#         a = f.readlines()
#         x, y = [], []
#         for i in a:
#             a, b = i.split()
#             x.append(a)
#             y.append(b)
#
# x = np.array(list(map(float, x)))
# y = np.array(list(map(float, y)))
#
# plt.legend(loc='best')
# plt.scatter(x, y, color='red', s=15)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

for i in ['dataXYZ_with_hindrance.txt']:
    with open(i) as f:
        a = f.readlines()
        x, y, z = [], [], []
        for i in a:
            a, b, c = i.split()
            x.append(a)
            y.append(b)
            z.append(c)

x = np.array(list(map(float, x)))
y = np.array(list(map(float, y)))
z = np.array(list(map(float, z)))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


# Plot the values
ax.scatter(x, y, z, c = 'b', marker='o')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

plt.show()