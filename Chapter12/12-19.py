import folium

m = folium.Map(location=[37.566679, 126.978291],
               zoom_start=13,
               width=640,
               height=480)

folium.Marker(location=
              [37.579754,126.976681]).add_to(m)
m
