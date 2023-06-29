import folium
import requests

# Create a base map
map = folium.Map(location=[37.7749, -122.4194], zoom_start=13)

folium.Marker(
    location=[37.7749, -122.4194],
    popup='Marker Popup Text',
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(map)

# Function to handle search requests


def search_location(search_query):
    api_key = '<5135f84fb07c4ecdb961e009e0b7d724>'
    url = f'https://api.opencagedata.com/geocode/v1/json?q={search_query}&key={api_key}'
    response = requests.get(url).json()

    if 'results' in response and len(response['results']) > 0:
        result = response['results'][0]
        lat = result['geometry']['lat']
        lon = result['geometry']['lng']
        folium.Marker(location=[lat, lon],
                      popup=result['formatted']).add_to(map)
        map.panTo([lat, lon])

        # Add a search control
folium.plugins.Search(control=False, search_zoom=15,
                      search_label='Search').add_to(map)


#
#
# Save the map as an HTML file
map.save('interactive_map.html')
