import create_playlist
import parse_saved_tracks
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
        self.all_tracks = user1.tracks + user2.tracks
        random.shuffle(self.all_tracks)


    def matchmake(self):
        print(f"{self.user1.username} now picking tracks.")
        likes1, superlike1 = parse_saved_tracks.choose_tracks_user1(self.user1.sp, self.all_tracks)
        print(f"{self.user2.username} now picking tracks.")
        likes2, superlike2 = parse_saved_tracks.choose_tracks_user1(self.user2.sp, self.all_tracks)
        superlikes = set(superlike1 + superlike2)
        self.common_liked = create_playlist.get_common_tracks(likes1, likes2, superlikes)
        print(f"You have {len(self.common_liked)} matches!")
        print(f"Now generating playlists...")
        create_playlist.gen_playlist(self.user1, self.user2, self.common_liked)
        time.sleep(1.5)
        print(f"Playlists made! It is now in your Spotify account. Thank you for using Spumble <3")



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