import numpy as np
import matplotlib.pyplot as plt

lst = [-20, 0, 20, 40, 60, 80, 100]
result = [(x - 32) * 5/9 for x in lst]
print(result)

plt.figure(figsize=(5,3))
plt.plot(lst, result)
plt.show()

#pro