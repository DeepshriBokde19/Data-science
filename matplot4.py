import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y1 = [0, 1, 4, 9, 16, 25]
y2 = [0, 1, 8, 27, 64, 125]
y3 = [0, 1, 16, 81, 256, 625]


plt.plot(x, y1, marker='o', linestyle='-', color='r', label='y = x^2')
plt.plot(x, y2, marker='s', linestyle='--', color='g', label='y = x^3')
plt.plot(x, y3, marker='^', linestyle=':', color='b', label='y = x^4')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Multiple Lines with Different Styles')

plt.legend()


plt.show()
