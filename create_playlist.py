'''
File: gen_playlist.py
-----------------------
This program generates a Spotify playlist between two users. The playlist 
consists of the songs that the two users both "Swipe Right" on plus an additional
two tracks depending on whether the "Super-Like" feature is used. 
'''

'''
Returns a list of tracks that both user1 and user2 liked. 
'''

def get_common_tracks(user1_liked, user2_liked, superlikes):
	user1_liked_tracks_set = set(user1_liked)
	common_tracks = user1_liked_tracks_set.intersection(user2_liked)
	return list(common_tracks.union(superlikes)) 

'''
This function just creates the playlist. I didn't realize this code would be
super short so I made a helper function but I don't think it is necessary anymore lol
'''
def gen_playlist(user1, user2, track_list):
	playlist_description = "This playlist was made using Spumble!"
	name = f"our spumble playlist: {user1.username} + {user2.username} <3"
	user1.sp.user_playlist_create(user=user1.username, name=name, public=True, collaborative=False, description=playlist_description)
	populate_playlist(user1, track_list)
	user2.sp.user_playlist_create(user=user2.username, name=name, public=True, collaborative=False, description=playlist_description)
	populate_playlist(user2, track_list)

'''
This function puts songs into the generated playlist (also v short my fault)
'''
def populate_playlist(user, track_list):
	playlist = user.sp.user_playlists(user=user.username)
	pid = playlist['items'][0]['id']
	user.sp.user_playlist_add_tracks(user=user.username, playlist_id=pid, tracks=track_list)
