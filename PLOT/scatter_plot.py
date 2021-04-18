import matplotlib.pyplot as plt
import numpy as np


x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([800,50,100,200,500,1000,60,90,10,300,600,800,75])
colors = np.array([4, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, s=sizes, c=colors, cmap='RdYlBu') #,
plt.text(10, 80, "Test", color = 'green', fontsize = 15)

plt.show()