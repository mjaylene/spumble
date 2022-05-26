import parse_saved_tracks
import spotipy
import spotipy.util as util
import time
import webbrowser

AUTH_SCOPE = 'user-library-read'
CLIENT_ID = '173887b931b446838389c5d09bd5ad70'
CLIENT_SECRET = '09808f452b32455f89da74a96ff7519e'
REDIRECT_URI = 'https://example.com/'
SPOTIFY_URL = "https://www.spotify.com/"

class MatchMaker:

    def __init__(self, user1, user2) -> None:
        self.user1 = user1
        self.user2 = user2


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