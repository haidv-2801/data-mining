import matplotlib.pyplot as plt
import numpy as np

a = [14.2, 16.4, 11.9, 15.2, 18.5, 22.1, 19.4, 25.1, 23.4, 18.1, 22.6, 17.2]
b = [215, 325, 185, 332, 406, 522, 412, 614, 544, 421, 445, 408]

plt.scatter(np.array(a),  np.array(b)) # vẽ biểu đồ scatter của 2 dãy a và b
plt.show()