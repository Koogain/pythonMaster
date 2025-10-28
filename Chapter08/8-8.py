import matplotlib.pyplot as plt

height = [165, 172, 158, 180, 170, 177, 160, 182, 155, 175]
weight = [55, 68, 50, 75, 60, 73, 52, 78, 48, 70]
gender = ['f', 'm', 'f', 'm', 'f', 'm', 'f', 'm', 'f', 'm']
color = ['#FFB2D9' if a=='f' else '#B5B2FF' for a in gender]

plt.figure(figsize=(5,3))
plt.scatter(height, weight, c=color)
plt.xlabel('height')
plt.ylabel('weight')
plt.show()