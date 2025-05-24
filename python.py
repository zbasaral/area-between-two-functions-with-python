
#y = x + 1 and y = (x/2)^2 Graphs
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 80) # x values
y_linear = x + 1 # y values
y_quadratic = (x / 2) ** 2
# plotting the graph, size of the graph
plt.figure(figsize=(10, 6))
# y = x + 1 ve y = (x/2)^2 draw funcitons with their properties
plt.plot(x, y_linear, color='pink', label='y = x + 1', marker='s', markersize=7)
plt.plot(x, y_quadratic, color='orange', label='y = (x/2)^2', marker='*', markersize=7)
# paint the space between functions
plt.fill_between(x, y_linear, y_quadratic, where=(y_linear >= y_quadratic), color='green', alpha=0.6)
# adding title and tag
plt.title('y = x + 1 and y = (x/2)^2 Graphs')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
# add arrows to the x and y axes
plt.annotate('', xy=(7, 0), xytext=(-10, 0),
             arrowprops=dict(arrowstyle='->', color='black'))
plt.annotate('', xy=(0, 13), xytext=(0, -5),
             arrowprops=dict(arrowstyle='->', color='black'))
# draw lines on the axes
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')

plt.xlim(-7, 7)   #define the boundaries
plt.ylim(-3, 13)
plt.grid()
plt.legend()
plt.show()
