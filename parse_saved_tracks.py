import random


"""
Get the saved tracks for the current user and put all the saved track uri's into a list.
Returns the list of saved track uri's. 
"""
def get_saved_tracks(sp):
	offset = 0
	tracks = []

	results = sp.current_user_saved_tracks(limit=50)
	while (results['items']):
		for item in results['items']:
			track = item['track']
			tracks.append(track['uri'])
		offset += 50
		results = sp.current_user_saved_tracks(limit=50, offset=offset)
	return tracks


'''
Given a list of Spotify track uri's, vote yes or no on a random 20 tracks. 
For now, I'm assuming users 1 and 2 don't go at the same time, so will populate all of user1's
"likes" into a list.
Returns a list of track uri's corresponding to user1's liked songs.
'''
def choose_tracks_user1(sp, tracks):
	likes = []
	superlike = []
	superliked = False
	for i in range(20):
		uri = tracks[i]
		track = sp.track(uri)
		print(track['artists'][0]['name'], " - ", track['name'])
		response = ''

		if (not superliked):
			response = input("yes, no, or SUPERLIKE? (y/n/s): " )
		else:
			response = input("yes or no? (y/n): " )

		if (response.lower() == "yes" or response.lower() == "y"):
			likes.append(uri)
		if ((response.lower() == 's' or response.lower() == 'SUPERLIKE') and not superliked):  # if they input superlike and didn't already superlike
			superlike.append(uri)
			superliked = True
		if ((response.lower() == 's' or response.lower() == 'SUPERLIKE') and superliked):
			likes.append(uri)
	return likes, superlike


def choose_tracks_user2(sp, my_tracks, other_tracks):
	matches = 0
	total_votes = 0
	matches_list = []

	while (matches < 5 and total_votes != len(my_tracks)):
		random_track = random.sample(my_tracks, 1)
		track = sp.track(random_track[0])
		print(track['artists'][0]['name'], " - ", track['name'])
		response = input("yes or no: ")
		if (response.lower() == "yes" or response.lower() == "y"):
			if random_track[0] in other_tracks:
				matches += 1
				matches_list.append(random_track[0])
		total_votes += 1

	return matches_list

