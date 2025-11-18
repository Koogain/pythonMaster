import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.core.display_functions import display

df = pd.read_csv("C:\\Users\\User\\PycharmProjects\\pythonMaster\\Chapter12\\지원자 정보(응답).csv")
# df = pd.DataFrame.from_records(rows=[1:], columns=rows[0])

df.rename(columns={'자격증 점수(기사:1000,산업기사:900,기능사:800)':'자격증 점수'}, inplace=True)
df.rename(columns={'희망 업무(복수 가능)':'희망 업무'}, inplace=True)

df['자격증 점수'] = df['자격증 점수'].astype(int)
df['토익 점수'] = df['토익 점수'].astype(int)

df.drop(columns='타임스탬프', inplace=True)

df['합계'] = df['자격증 점수'] + df['토익 점수']

df['결과'] = np.where(df['합계']>=1500, '합격', '불합격')

display(df['결과']=='합격')

# df.to_csv('result.csv', index=False)

desired_work = {'개발':0, '기획':0, '경영':0, '영업':0}

for s in df['희망 업무']:
    for a in s.split(','):
        desired_work[a.strip()] += 1

for key, value in desired_work.items():
    print(key, value)


plt.figure(figsize=(5, 3))
ind = np.arange(len(desired_work))
plt.bar(ind, desired_work.values())
plt.xticks(ind, desired_work.keys())
plt.show()

# display(df)
