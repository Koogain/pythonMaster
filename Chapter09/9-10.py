import numpy as np
import matplotlib.pyplot as plt

year = [2006, 2009, 2012, 2015, 2018]
kor = [547, 546, 554, 524, 526]

plt.figure(figsize=(5,3))
plt.plot(year, kor)
plt.ylim(500, 580)
plt.xlabel('year')
plt.ylabel('score')
plt.show()