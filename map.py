# import libraries
import requests
import folium

# API for ISS position
url = "http://api.open-notify.org/iss-now.json"

# get data from API
response = requests.get(url)
data = response.json()

# get coordinates
lat = float(data["iss_position"]["latitude"])
lon = float(data["iss_position"]["longitude"])

# print coordinates
print("ISS position:")
print("Latitude:", lat)
print("Longitude:", lon)

# create map
m = folium.Map(location=[lat, lon], zoom_start=3)

# add marker
folium.Marker([lat, lon], popup="ISS").add_to(m)

# save map
m.save("iss_kart.html")

print("Map saved as iss_kart.html")