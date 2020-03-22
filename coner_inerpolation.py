import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

list_for_x = list()
list_for_y = list()

x1 = np.linspace(0, 50, 1000)
y1 = -0.7 * x1 + 50

list_previous_x = [element for element in x1 if element < 26]
list_previous_y = [-0.7 * element + 50 for element in list_previous_x]

list_for_x = [element for element in x1 if element > 25 and element < 61][::100]
list_for_y = [-0.7 * element + 50 for element in list_for_x]

x2 = np.linspace(50, 200, 1000)
y2 = x1 / x1 * 15

[list_for_x.append(element) for element in x2 if element > 60 and element < 70]
[list_for_y.append(element/element * 15) for element in list_for_x if element > 60 and element < 70]

list_next_x = [element for element in x2 if element > 70]
list_next_y = [element/element * 15 for element in list_next_x]


f = interp1d(list_for_x, list_for_y, kind='cubic')
xnew = np.linspace(list_for_x[0], list_for_x[-1], num = 100, endpoint=True)


fig, axes = plt.subplots(1, 2, figsize=(13,8))
axes[0].plot(x1, y1, '-', x2, y2, '-', color='g')
axes[1].plot(xnew, f(xnew), '-', list_previous_x, list_previous_y, '-',\
    list_next_x, list_next_y, '-', color='g')

plt.show()
