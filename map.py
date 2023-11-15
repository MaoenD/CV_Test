import streamlit as st
import folium
from geopy.geocoders import Nominatim

# Define the locations
locations = [
    {"name": "Location 1", "address": "1031 Valencia Street, San Francisco, CA 94110"},
    {"name": "Location 2", "address": "43 Rue des Tartres, 92500, Rueil-Malmaison"},
    {"name": "Location 3", "address": "Le Surena, Face au 5 Quai Marcel Dassault, 92150 SURESNES"},
]

# Function to geocode an address
geolocator = Nominatim(user_agent="cv_app")
def geocode_location(address):
    location = geolocator.geocode(address)
    if location:
        return [location.latitude, location.longitude]
    return None

def display_map(locations):
    m = folium.Map(location=[48.8566, 2.3522], zoom_start=5)  # Centered on France

    for loc in locations:
        coordinates = geocode_location(loc["address"])
        if coordinates:
            folium.Marker(
                location=coordinates,
                popup=loc["name"],
            ).add_to(m)

    st.write(m)

if __name__ == "__main__":
    display_map(locations)
