import pandas as pd
import folium

df = pd.DataFrame({'이름':['경복궁', '덕수궁', '창경궁', '창덕궁'],
                   '위도':[37.570754, 37.566167, 37.580246, 37.582387],
                   '경도':[126.976681, 126.97517, 126.994833, 126.991701]})

m = folium.Map(location=[37.566679, 126.978291],
               zoom_start=13,
               width=640,
               height=480)

for _, row in df.iterrows():
    folium.Marker([row['위도'], row['경도']], tooltip=row['이름']).add_to(m)
m.save('seoul.html')
m