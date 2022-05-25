'''
File: gen_playlist.py
-----------------------
This program generates a Spotify playlist between two users. The playlist 
consists of the songs that the two users both "Swipe Right" on plus an additional
two tracks depending on whether the "Super-Like" feature is used. 
'''

import auth
#from parse_saved_tracks import choose_tracks_user1, get_saved_tracks
#from auth import username

auth.init()

'''
Returns a list of tracks that both user1 and user2 liked. 

def get_common_tracks():
	# Also pretty bogus because user1 and user2 would have different tracks but 
	# I will fix this when later, I promise!!
	tracks = get_saved_tracks() 

	user1_liked_tracks = choose_tracks_user1(tracks)
	user2_liked_tracks = choose_tracks_user2(tracks)
	
	user1_liked_tracks_set = set(user1_liked_tracks)
	common_tracks = user1_liked_tracks_set.intersection(user2_liked_tracks)
	return list(common_tracks)
'''

'''
This function just creates the playlist. I didn't realize this code would be
super short so I made a helper function but I don't think it is necessary anymore lol
'''
def gen_playlist(username, name):
	playlist_description = "This playlist was made using Spumble!"
	auth.sp.user_playlist_create(user=username, name=name, public=True, collaborative=False, description=playlist_description)

'''
This function puts songs into the generated playlist (also v short my fault)
'''
def populate_playlist(username, track_list):
	playlist = auth.sp.user_playlists(user=username)
	pid = playlist['items'][0]['id']
	auth.sp.user_playlist_add_tracks(user=username, playlist_id=pid, tracks=track_list)

def main():
	#tracks = get_saved_tracks()
	#common_tracks = choose_tracks_user1(tracks)
	# NOTE: Just did this for now since we don't have a list of common songs yet
	result = auth.sp.search(q="Promiscuous") 
	username = 'jayjaymobbles' # NOTE: Also just for now cuz i was confused on how to get this
	common_tracks = []
	common_tracks.append(result['tracks']['items'][0]['uri'])
	#common_tracks = get_saved_tracks()
	playlist_name = "Our Spumble Playlist"
	gen_playlist(username, playlist_name)
	populate_playlist(username, common_tracks)


if __name__ == '__main__':
	main()

