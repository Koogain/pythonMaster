import matplotlib.pyplot as plt

year = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
gdp = [3079.9, 3170.5, 3270.8, 3375.2, 3480.0, 3585.4, 3500.1, 3620.3, 3700.7]

plt.figure(figsize=(5,3))
plt.plot(year, gdp, 'g.-')
plt.title('GDP percapita')
plt.xlabel('year')
plt.ylabel('ten thousand won')
plt.ylim(2500, 4500)
plt.show()