import pandas as pd
from geopy.geocoders import Nominatim
import folium

geolocator = Nominatim(user_agent='Jeju v1.0')
center = geolocator.geocode('서울특별시')

df = pd.DataFrame()
df['이름'] = ['국립중앙박물관', '국립민속박물관', '서울역사박물관', '국립고궁박물관']

lat = []
lng = []
for _, row in df.iterrows():
    loc = geolocator.geocode(row['이름'])
    lat.append(loc.latitude)
    lng.append(loc.longitude)

df['위도'] = lat
df['경도'] = lng

m = folium.Map(location=[center.latitude, center.longitude],
               zoom_start=12,
               tiles='cartodb positron',
               width=640,
               height=480)

for _, row in df.iterrows():
    folium.Marker([row['위도'], row['경도']], tooltip=row['이름']).add_to(m)
m.save('seoul.html')
m