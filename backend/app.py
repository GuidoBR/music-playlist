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
    base_request = "track.search?format=json&callback=callback&quorum_factor=1&apikey={}&q_lyrics=".format(MUSIX_API_KEY)
    music_request = "{}{}{}".format(BASE_MUSIC_URL, base_request, lyrics)
    
    response = {"track_1": {}, "track_2": {}}
    try:
        r = requests.get(music_request)
        track_list = r.json().get('message').get('body').get('track_list')

        response['track_1'] = track_list[0]
        response['track_2'] = track_list[1]

        return response
    except:
        return 'Error requesting track list, try again later'
    
