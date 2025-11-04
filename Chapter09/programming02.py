import numpy as np
import matplotlib.pyplot as plt

year = [2006, 2009, 2012, 2015, 2018]
korea = [547, 546, 554, 524, 526]
usa = [474, 472, 565, 478, 470]
japan = [523, 529, 536, 532, 527]

ind = np.arange(len(year))

w = 0.3
plt.figure(figsize=(6, 3.5))
plt.bar(ind-w/3+0.4, korea, color='b', width=w, label='korea')
plt.bar(ind-w/3+0.6, usa, color='g', width=w, label='uas')
plt.bar(ind-w/3+0.8, japan, color='r', width=w, label='japan')
plt.xticks(ind, year)
plt.legend()
plt.xlabel('year')
plt.ylabel('score')
plt.show()