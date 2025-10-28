import matplotlib.pyplot as plt

seoson = {'spring', 'summer', 'autumn', 'winter'}
precipitation = {330.5, 612.8, 256.4, 13.3}

plt.figure(figsize=(5,3))
plt.bar(seoson, precipitation)
plt.title('precipitation')
plt.ylabel('mn')
plt.show()