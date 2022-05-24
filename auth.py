"""
Handle all Spotify authentication stuff by importing auth and running auth.init().

"""
import spotipy
import spotipy.util as util

username = 'fabian12062001'
AUTH_SCOPE = 'user-library-read user-read-recently-played'
CLIENT_ID = '173887b931b446838389c5d09bd5ad70'
CLIENT_SECRET = '09808f452b32455f89da74a96ff7519e'
REDIRECT_URI = 'https://example.com/'

def init():
    global sp
    token = util.prompt_for_user_token(username, scope=AUTH_SCOPE, client_id = CLIENT_ID, client_secret = CLIENT_SECRET, redirect_uri = REDIRECT_URI)
    sp = spotipy.Spotify(auth=token)