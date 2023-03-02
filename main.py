import phonenumbers
import opencage

import folium
from phonenumber import number

from api import API_KEY # I use api of open cage .


from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,"en")
print(location)
from phonenumbers import carrier

service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode


geocoder = OpenCageGeocode(API_KEY)
value = str(location)
results = geocoder.geocode(value)
#print(results)


lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat , lng)

myMap = folium.Map(location= [lat, lng], zoom_start = 9)

folium.Marker([lat, lng], popup = location).add_to(myMap)

myMap.save("ShowMyLOcation.html")  # after running this code , a new html file will be generated in the same folder where this pyhton file is placed

# just simply open that html file on live server then it give the location 