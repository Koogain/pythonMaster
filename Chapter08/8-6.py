import matplotlib.pyplot as plt

year = [2000, 2005, 2010, 2015, 2020, 2025]
single_household = [2220000, 3050000, 4140000, 5200000, 6640000, 7500000]  # 1인 가구 수
births = [640000, 450000, 470000, 438000, 272000, 230000]  # 출생아 수

plt.figure(figsize=(5,3))
plt.scatter(single_household, births)
plt.xlabel('single-person household ratio')
plt.ylabel('the number of babies born')
plt.show()