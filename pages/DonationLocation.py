import streamlit as st
import pandas as pd

def get_blood_stock():
    # Example placeholder, replace with real data scraping
    return pd.DataFrame({
        'Blood Type': ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-'],
        'Stock Level': ['Low', 'Moderate', 'High', 'Moderate', 'Low', 'High', 'Low', 'Moderate']
    #to try and scrap (last feature to add)
    })

import streamlit as st
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import folium
from streamlit_folium import st_folium

# Sample data: blood bank locations (name, latitude, longitude)
blood_banks = [
    {"name": "Bloodbank@HSA", "latitude": 1.287953, "longitude": 103.846937},
    {"name": "Bloodbank@Dhoby Ghaut", "latitude": 1.299065, "longitude": 103.845434},
    {"name": "Bloodbank@Woodlands", "latitude": 1.436065, "longitude": 103.786278},
    {"name": "Bloodbank@Westgate Tower", "latitude": 1.335947, "longitude": 103.742879},
    {"name": "Bloodbank@One Punggol", "latitude": 1.408639, "longitude": 103.905044}
]

# Function to geocode postal code to latitude and longitude
def geocode_postal_code(postal_code):
    geolocator = Nominatim(user_agent="blood_donation_app")
    location = geolocator.geocode(f"{postal_code}, Singapore")
    if location:
        return (location.latitude, location.longitude)
    return None

# Function to find the nearest blood bank
def find_nearest_blood_bank(user_location):
    nearest_bank = None
    min_distance = float("inf")
    for bank in blood_banks:
        bank_location = (bank["latitude"], bank["longitude"])
        distance = geodesic(user_location, bank_location).kilometers
        if distance < min_distance:
            min_distance = distance
            nearest_bank = bank
    return nearest_bank, min_distance

def main():
    st.title("Where to Donate Blood")
    
    # Display blood stock levels and map (Placeholder content)

    st.write("Interactive map showing bloodbank locations:")
    # Display map with all blood banks
map_center = (1.3521, 103.8198)  # Center of Singapore
blood_map = folium.Map(location=map_center, zoom_start=11)

# Add markers for each blood bank
for bank in blood_banks:
    folium.Marker(
        location=(bank["latitude"], bank["longitude"]),
        popup=bank["name"],
        icon=folium.Icon(color="red")
    ).add_to(blood_map)

# Display the map with blood banks
st.write("**Blood Banks in Singapore**")
st_folium(blood_map, width=700, height=500)

# Ask for user's postal code
st.write("Enter your address to find the nearest blood bank:")
postal_code = st.text_input("Address:")

if postal_code:
    user_location = geocode_postal_code(postal_code)
    if user_location:
        # Find the nearest blood bank
        nearest_bank, distance = find_nearest_blood_bank(user_location)
        
        # Display nearest blood bank information
        st.write(f"**Nearest Blood Bank:** {nearest_bank['name']}")
        st.write(f"**Distance:** {distance:.2f} km")
        
        # Add user location and nearest bank to a new map
        nearest_map = folium.Map(location=user_location, zoom_start=12)
        
        # Mark user's location
        folium.Marker(
            location=user_location,
            popup="Your Location",
            icon=folium.Icon(color="blue")
        ).add_to(nearest_map)
        
        # Mark nearest blood bank
        folium.Marker(
            location=(nearest_bank["latitude"], nearest_bank["longitude"]),
            popup=nearest_bank["name"],
            icon=folium.Icon(color="green")
        ).add_to(nearest_map)
        
        # Display the map with user's location and nearest blood bank
        st.write("**Your Location and Nearest Blood Bank**")
        st_folium(nearest_map, width=700, height=500)
    else:
        st.error("Could not find the location for the given postal code. Please try again.")

if __name__ == "__main__":
    main()

