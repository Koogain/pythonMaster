import matplotlib.pyplot as plt

height = [165, 172, 158, 180, 170, 177, 160, 182, 155, 175]
weight = [55, 68, 50, 75, 60, 73, 52, 78, 48, 70]
gender = ['f', 'm', 'f', 'm', 'f', 'm', 'f', 'm', 'f', 'm']

plt.figure(figsize=(5,3))
plt.scatter(height, weight)
plt.xlabel('height')
plt.ylabel('weight')
plt.show()