import auth

auth.init()
sp = auth.sp

results = sp.current_user_saved_tracks(limit=20)
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])