import matplotlib.pyplot as plt


x_values = [0, 6]
y_values = [0, 250]


plt.plot(x_values, y_values, marker='o')


plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Line from (0,0) to (6,250)')


plt.show()
