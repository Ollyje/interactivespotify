import spotipy
import json
import urllib.request
import spotipy.util as util
import json

creds = "spotifykeys.json"
with open(creds, 'r') as keys:
	api_tokens = json.load(keys)

client_id = api_tokens['client_id']
client_secret = api_tokens['client_secret']
redirectURI = api_tokens['redirect']
username = api_tokens['username']

scope = 'user-read-private user-read-playback-state user-modify-playback-state playlist-modify-public user-library-read'
token = util.prompt_for_user_token(username, scope, client_id=client_id,
                           client_secret=client_secret,
                           redirect_uri=redirectURI)

sp = spotipy.Spotify(auth=token)


def get_limit(limit, keyword):

	track_results = sp.search(q=keyword, type='track', limit=limit)

	tracks = track_results['tracks']['items']
	
	songs = []
	for track in tracks:
		songs.append(track['uri'])

		# if track_results['tracks']['items'][0]['uri'] not in songs:
			# songs.append(track_results['tracks']['items'][0]['uri'])

	my_playlist = sp.user_playlist_create(user=username, name='fire', public=True, description='description')
	results = sp.user_playlist_add_tracks(username, my_playlist['id'], songs)

	return my_playlist['id']

# i feel like i need to use the len function in here somewhere?
