import numpy as np
import matplotlib.pyplot as plt

year = [2000, 2005, 2010, 2015, 2020]
solo_live = [15.5, 20.0, 23.9, 27.2, 31.7]
birth = [640089, 438707, 478420, 438420, 272337]

plt.figure(figsize=(5,3))
plt.plot(year, birth)
plt.ylabel('the number of babies born')
plt.legend()
plt.show()

plt.figure(figsize=(5, 3))
plt.scatter(solo_live, birth, s=20)
plt.legend()
plt.xlabel('the proportion of single-person households')
plt.ylabel('the number of babies born')
plt.show()