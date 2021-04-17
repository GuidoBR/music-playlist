from flask import Flask
import requests
import os

app = Flask(__name__)

BASE_MUSIC_URL = "https://api.musixmatch.com/ws/1.1/"
MUSIX_API_KEY = os.environ.get('MUSIX_API_KEY')

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/track/search/<lyrics>')
def search(lyrics: str) -> str:
    base_request = "track.search?format=jsonp&callback=callback&quorum_factor=1&apikey={}&q_lyrics=".format(MUSIX_API_KEY)
    music_request = "{}{}{}".format(BASE_MUSIC_URL, base_request, lyrics)

    r = requests.get(music_request)
    return r.content
