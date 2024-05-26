import matplotlib.pyplot as plt

# Define the x and y values
x_values = [1, 8]
y_values = [3, 10]

# Create the plot
plt.plot(x_values, y_values, marker='o')

# Set the labels and title
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Line from (1,3) to (8,10)')

# Display the plot
plt.show()
