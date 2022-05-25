import auth
import random

auth.init()

"""
Get the saved tracks for the current user and put all the saved track uri's into a list.
Returns the list of saved track uri's. 
"""
def get_saved_tracks():
	offset = 0
	tracks = []

	results = auth.sp.current_user_saved_tracks(limit=50)
	while (results['items']):
		for item in results['items']:
			track = item['track']
			tracks.append(track['uri'])
		offset += 50
		results = auth.sp.current_user_saved_tracks(limit=50, offset=offset)
	return tracks


'''
Given a list of Spotify track uri's, vote yes or no on a random 20 tracks. 
For now, I'm assuming users 1 and 2 don't go at the same time, so will populate all of user1's
"likes" into a list.
Returns a list of track uri's corresponding to user1's liked songs.
'''
def choose_tracks_user1(tracks):
	likes = []
	for i in range(20):
		random_track = random.sample(tracks, 1)
		track = auth.sp.track(random_track[0])
		print(track['artists'][0]['name'], " - ", track['name'])
		response = input("yes or no: ")
		if (response.lower() == "yes" or "y"):
			likes.append(random_track[0])
	return likes


def main():
	# uncomment these lines to see it in action:
    #tracks = get_saved_tracks()
   	#choose_tracks_user1(tracks)
    

if __name__ == '__main__':
    main()