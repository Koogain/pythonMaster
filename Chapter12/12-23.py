from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='Jeju v1.0')

loc = geolocator.geocode('경복궁')
print(loc.latitude)
print(loc.longitude)
print(loc.address)
