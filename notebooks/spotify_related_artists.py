import requests

main_api = "https://accounts.spotify.com/api/token"
CLIENT_ID = "cba2e4711180476cbfc30b9730244281"
CLIENT_SECRET = "b69aa46be05a4fffb4ada07e7f6b986e"

def get_access_token():
    auth_response = requests.post(main_api, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    return access_token

def get_related_artists(artist_name):
    access_token = get_access_token()
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    
    BASE_URL = 'https://api.spotify.com/v1/'
    
    # Search for the artist
    search_response = requests.get(BASE_URL + 'search', headers=headers, params={'q': artist_name, 'type': 'artist', 'limit': 1})
    
    if search_response.status_code == 200:
        search_data = search_response.json()
        if search_data['artists']['items']:
            artist_id = search_data['artists']['items'][0]['id']
    
            # Get related artists
            related_response = requests.get(BASE_URL + 'artists/' + artist_id + '/related-artists', headers=headers)
    
            if related_response.status_code == 200:
                related_data = related_response.json()
                related_artists = [artist['name'] for artist in related_data['artists']]
                return ", ".join(related_artists)
            else:
                return "Error fetching related artists. Status code: {}".format(related_response.status_code)
        else:
            return "Artist not found."
    else:
        return "Error occurred while searching for the artist. Status code: {}".format(search_response.status_code)
