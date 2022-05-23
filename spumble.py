import spotipy
import spotipy.util as util

username = 'fabian12062001'
AUTH_SCOPE = 'user-library-read'
CLIENT_ID = '173887b931b446838389c5d09bd5ad70'
CLIENT_SECRET = '09808f452b32455f89da74a96ff7519e'
REDIRECT_URI = 'https://example.com/'

token = util.prompt_for_user_token(username, AUTH_SCOPE, client_id = CLIENT_ID, client_secret = CLIENT_SECRET, redirect_uri = REDIRECT_URI)

urn = 'https://open.spotify.com/artist/2YZyLoL8N0Wb9xBt1NhZWg?si=wiWvPAFMQYSWSX7pUo0Ikw'
sp = spotipy.Spotify(auth=token)

artist = sp.artist(urn)
print(artist)