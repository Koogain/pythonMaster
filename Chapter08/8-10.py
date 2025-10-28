import matplotlib.pyplot as plt

name = ['Jessica', 'Lima', 'sophia']
x = [75, 92, 83]
y = [79, 89, 90]

plt.figure(figsize=(5,3))
plt.scatter(x,y)
for i in range(len(name)):
    plt.annotate(name[i],xy=(x[i],y[i]),xytext=(5,-10),textcoords='offset points')
plt.xlim(73, 95)
plt.ylim(75, 93)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()