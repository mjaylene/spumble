import requests
from flask import Flask, render_template
from wordcloud import WordCloud


app = Flask(__name__)
wc = WordCloud(
    background_color="white",
    max_words=100,
    colormap='plasma',
    width=1000,
    height=800
)


@app.route('/<wiki_slug>', methods=['GET'])
def wordcloud(wiki_slug):
    r = requests.get(f'https://en.wikipedia.org/w/api.php?action=query&format=json&titles={wiki_slug}&prop=extracts&explaintext')
    data = r.json()

    page_id, page_data = data['query']['pages'].popitem()
    if page_id == '-1':
        return 'No such document', 404

    img_data = wc.generate(page_data['extract']).to_svg()
    return render_template('display.html', img_data=img_data)



'''
build a Flask application that uses render_page to deliver HTML content to each user. 

Then, when a user visits the website, you ask them to enter their spotify username and their Spotify Authentication 
Token (more on this later—but this essentially functions like the user’s password). 

Then, you can create a new file on the server end, where you store all of their data. So, you might have a folder on the server called, 
say, data/ and then you use the Python file commands we’ve learned to create files like data/psarin.json, and put all 
of the information for my user in there. 

That file could contain my authentication token, 
but it might also contain all of the songs i’ve rated in the past or the other users that I’m friends with or …

'''