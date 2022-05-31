import create_playlist
import parse_saved_tracks
from music_player import create_match_window, create_close_window
import random
import spotipy
import spotipy.util as util
import time
import webbrowser

AUTH_SCOPE = 'user-library-read playlist-modify-public'
CLIENT_ID = '173887b931b446838389c5d09bd5ad70'
CLIENT_SECRET = '09808f452b32455f89da74a96ff7519e'
REDIRECT_URI = 'https://example.com/'
SPOTIFY_URL = "https://www.spotify.com/"


class MatchMaker:

    def __init__(self, user1, user2) -> None:
        self.user1 = user1
        self.user2 = user2
        user1_tracks = user1.tracks
        random.shuffle(user1_tracks)
        user2_tracks = user2.tracks
        random.shuffle(user2_tracks)
        self.all_tracks = user1_tracks[:10] + user2_tracks[:10]


    def matchmake(self):
        likes1, superlike1 = create_match_window(self.user1.username, self.user1.sp, self.all_tracks)
        likes2, superlike2 = create_match_window(self.user2.username, self.user2.sp, self.all_tracks)
        superlikes = set(superlike1 + superlike2)
        self.common_liked = create_playlist.get_common_tracks(likes1, likes2, superlikes)
        create_playlist.gen_playlist(self.user1, self.user2, self.common_liked)
        create_close_window(self.common_liked)        


class User:

    def __init__(self, username) -> None:
        self.username = username
        self.authorize()
        self.sp = spotipy.Spotify(auth=self.token)
        self.tracks = parse_saved_tracks.get_saved_tracks(self.sp)

    def authorize(self):
        print(f"Running authentication for {self.username}")
        time.sleep(1.5)
        token = util.prompt_for_user_token(username=self.username, scope=AUTH_SCOPE, 
                                           client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                           redirect_uri=REDIRECT_URI)
        self.token = token
        print(f"Authentication complete. Please make sure to open up Spotify in your web browser and log out.")
        input("Press enter when done.")