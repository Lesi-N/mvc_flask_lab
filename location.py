import json
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable
import folium


def read_file(file_path):
    '''
    Reads json file
    '''
    file = open(file_path, mode='r').readlines()
    file = [f.strip() for f in file]
    file = ''.join(file)
    return json.loads(file)


def get_locations(file):
    users = read_file(file)['users']
    locations = []
    for user in users:
        if user['location'] != '':
            locations.append([user['screen_name'], user['location']])
    return locations


def convert_to_coordinates(location):
    try:
        geolocator = Nominatim(user_agent='Follower_map')
        coordinates = geolocator.geocode(location)
        return (coordinates.latitude, coordinates.longitude)
    except (AttributeError, GeocoderUnavailable):
        pass


def create_map(locations_list):
    for loc in locations_list:
        coord = convert_to_coordinates(loc[1])
        if coord == None:
            locations_list.pop(locations_list.index(loc))
        else:
            loc.append(coord)
    start_location = [38.653671, -16.233521]
    follower_map = folium.Map(location=start_location, zoom_start=3)
    for loc in locations_list:
        try:
            folium.Marker(location=loc[2], popup=loc[0], icon=folium.Icon(color="darkpurple")).add_to(follower_map)
        except IndexError:
            continue
    folium.TileLayer('cartodbdark_matter').add_to(follower_map)
    folium.TileLayer('stamenterrain').add_to(follower_map)
    folium.LayerControl().add_to(follower_map)
    return follower_map


def generate_map(file):
    locations = get_locations(file)
    return create_map(locations)


