import spotipy
import spotipy.util as util

# username = 'fabian12062001'
AUTH_SCOPE = 'user-library-read'
CLIENT_ID = '173887b931b446838389c5d09bd5ad70'
CLIENT_SECRET = '09808f452b32455f89da74a96ff7519e'
REDIRECT_URI = 'https://example.com/'


"""
Returns list of a single attribute, specified by info_wanted, of all saved tracks in a user's library.

info_wanted options: album, artists,available_markets, disc_number, duration_ms, explicit, external_ids,
                     external_urls, href, id, is_local, name, popularity, preview_url, track_number, type, uri
"""
def get_saved_tracks_info(sp_spotify, info_wanted):
    tracks_left = True
    saved_tracks_info = []
    previous_len = -1
    limit = 50 # max limit is 50, default is 20
    offset = 0
    while tracks_left:
        saved_tracks = sp_spotify.current_user_saved_tracks(limit=limit, offset=offset) # max limit is 50, default is 20
        if len(saved_tracks_info) == previous_len:
            tracks_left = False
        for entry in saved_tracks['items']:
            saved_tracks_info.append(entry['track'][info_wanted])
            if len(saved_tracks_info) == previous_len:
                tracks_left = False
                break
            else:
                previous_len = len(saved_tracks_info)
        offset += limit
    return saved_tracks_info


def main():
    # username = input('Enter your Spotify username: ')
    username = 'fabian12062001'
    token = util.prompt_for_user_token(username, AUTH_SCOPE, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)
    sp = spotipy.Spotify(auth=token)
    saved_tracks = get_saved_tracks_info(sp, 'name')
    print(len(saved_tracks))
    print(saved_tracks)


if __name__ == '__main__':
    main()