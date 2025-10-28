import matplotlib.pyplot as plt

preci = {'spring':330.5, 'summer':612.8, 'autumn':256.4, 'winter':13.3}

plt.figure(figsize=(5,3))
plt.bar(preci.keys(),preci.values())
plt.title('precipitation')
plt.ylabel('mn')
plt.show()