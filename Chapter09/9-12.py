import numpy as np
import matplotlib.pyplot as plt

nation = ['Korean', 'USA', 'Japen', 'France']
men = [175.5, 176.9, 172.1, 178.6]
women = [163.2, 163.3, 158.4, 164.5]
ind = np.arange(len(nation))

plt.figure(figsize=(5,3))
plt.bar(ind, men, color='b', width=0.4, label='men')
plt.bar(ind, women, color='r', width=0.4, label='women')
plt.ylim(130, 190)
plt.title('Height')
plt.ylabel('cm')
plt.xticks(int,nation)
plt.legend()
plt.show()