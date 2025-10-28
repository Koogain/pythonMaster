import matplotlib.pyplot as plt

monthly_temperatures = [
    0.2,   # 1월
    1.5,   # 2월
    6.3,   # 3월
    12.1,  # 4월
    17.6,  # 5월
    22.5,  # 6월
    25.7,  # 7월
    26.1,  # 8월
    21.3,  # 9월
    15.0,  # 10월
    7.8,   # 11월
    1.9    # 12월
]

plt.figure(figsize=(5,3))
plt.hist(monthly_temperatures, bins=15, alpha=0.5)
plt.xlabel('temperature')
plt.ylabel('frequency')
plt.show()