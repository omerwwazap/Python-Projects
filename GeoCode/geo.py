# If possible find a way to do this in javascript
# Add javascript version to my github page for daily use projects
#

from geopy.geocoders import Nominatim
geolocation = Nominatim(user_agent="omerwwazap_testing")

place_name = input("Enter place name: ")

location = geolocation.geocode(place_name)

print(location)