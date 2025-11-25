import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
from geopy.geocoders import Nominatim

df = pd.read_csv(
    "C:\\Users\\User\\PycharmProjects\\pythonMaster\\Chapter12\\제주도 관광(응답).csv",
    encoding="utf-8-sig"
)

# 컬럼 이름에서 BOM · 공백 · 따옴표 전부 제거
df.columns = df.columns.str.replace('\ufeff', '').str.strip().str.replace('"','')

print(df.columns.tolist())

# 방문 관광지 수 계산
result = {'마라도':0, '만장굴':0, '한라산':0, '산굼부리':0, '정방폭포':0, '성산일출봉':0, '천지연폭포':0}
for x in df['방문한 관광지(복수 가능)']:
    for a in x.split(','):
        result[a] += 1

# 그래프
ind = np.arange(len(result))
plt.figure(figsize=(6, 3))
plt.bar(ind, result.values(), width=0.7)
plt.ylabel('방문자수')

# DataFrame 구성
df2 = pd.DataFrame({
    '이름': result.keys(),
    '방문자수': result.values()
})

# 위치 정보 추가
geolocator = Nominatim(user_agent='Jeju v1.0')

lat_list = []
lon_list = []

for _, row in df2.iterrows():
    loc = geolocator.geocode(row['이름'])
    lat_list.append(loc.latitude)
    lon_list.append(loc.longitude)

df2['위도'] = lat_list
df2['경도'] = lon_list

# 지도 생성
center = geolocator.geocode('제주도')
m = folium.Map(location=[center.latitude, center.longitude],
               width=640,
               height=480)

# 마커 표시
for _, row in df2.iterrows():
    folium.Marker([row['위도'], row['경도']], tooltip=row['이름']).add_to(m)

m.save('seoul.html')
m
