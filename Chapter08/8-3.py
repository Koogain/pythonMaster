import matplotlib.pyplot as plt

year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
seoul = [12.5, 12.7, 12.9, 13.1, 13.3, 13.5, 13.7, 13.9, 14.1, 14.3, 14.5, 14.7, 14.9]
jeju = [16.2, 16.4, 16.6, 16.8, 17.0, 17.2, 17.4, 17.6, 17.8, 18.0, 18.2, 18.4, 18.6]


plt.figure(figsize=(5,3))
plt.plot(year, seoul, label='seoul')
plt.plot(year, jeju, label='jeju')
plt.ylim(10,20)
plt.title('temperature')
plt.xlabel('year')
plt.legend()
plt.show()