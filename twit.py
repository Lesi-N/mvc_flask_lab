import requests
import json

def get_user_info(handle, bearer):
    base_url = 'https://api.twitter.com/'

    search_url = '{}1.1/friends/list.json'.format(base_url) #endpoint

    search_headers = {
        'Authorization': 'Bearer {}'.format(bearer)
    }

    search_params = {
        'screen_name': handle,
        'count': 28
    }

    response = requests.get(search_url, headers=search_headers, params=search_params)

    json_response = response.json()
    return json_response

def write_to_file(info):
    with open('user_info.json', mode='w') as file:
        json.dump(info, file, indent=4)
    return

