import folium
import geojson


# base map
latitude = 35.710063
longitude = 139.8107
name = "Tokyo Skytree"


map = folium.Map(location=[35.710063, 139.8107],
                 zoom_start=18)  # Create the map


folium.Marker(location=[35.710063, 139.8107], popup=name).add_to(
    map)  # Add a marker for Tokyo Skytree

gemstone_coordinates = [139.809723, 35.710072]  # Longitude, Latitude
gemstone_point = geojson.Point(gemstone_coordinates)

# Create a GeoJSON feature collection with the gemstone point
feature_collection = geojson.FeatureCollection(
    [geojson.Feature(geometry=gemstone_point)])

# Save the GeoJSON data to a file
with open('c:\python311\lib\site-packages', 'w') as f:
    f.write(geojson.dumps(feature_collection))

map.save('map_skytree.html')
