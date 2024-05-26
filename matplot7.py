import matplotlib.pyplot as plt


y_values = [3, 10]


plt.scatter(x_values, y_values, color='red')


plt.text(1, 3, '(1, 3)', fontsize=12, ha='right')
plt.text(8, 10, '(8, 10)', fontsize=12, ha='right')


plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Points at (1, 3) and (8, 10)')


plt.show()
