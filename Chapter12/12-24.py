from geopy.geocoders import Nominatim
import folium

geolocator = Nominatim(user_agent='Jeju v1.0')
center = geolocator.geocode('서울특별시')
name = '경복궁'
loc = geolocator.geocode(name)

m = folium.Map(location=[center.latitude, center.longitude],
               zoom_start=12,
               width=640,
               height=480
)

folium.Marker([loc.latitude, loc.longitude], tooltip=name).add_to(m)
m.save('seoul.html')
m