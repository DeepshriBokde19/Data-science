import matplotlib.pyplot as plt


x_values = []
y_values = []
with open('test.txt', 'r') as file:
    for line in file:
        x, y = map(float, line.split())
        x_values.append(x)
        y_values.append(y)


plt.plot(x_values, y_values, marker='o')


plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Line from text file data')


plt.show()
