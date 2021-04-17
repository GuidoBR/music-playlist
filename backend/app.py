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
    
    try:
        r = requests.get(music_request)
        track_list = r.json().get('message').get('body').get('track_list')

        musics = {}
        for track in track_list:
            music = track.get('track')
            lyrics_request_url = "track.lyrics.get?format=json&callback=callback&quorum_factor=1&apikey={}&track_id=".format(MUSIX_API_KEY)
            lyrics_request = "{}{}{}".format(BASE_MUSIC_URL, lyrics_request_url, music.get('track_id'))
            r = requests.get(lyrics_request)
            lyrics_track = r.json().get('message').get('body').get('lyrics').get('lyrics_body')

            musics['track_1'] = {
                'track_name': music.get('track_name'),
                'lyrics': lyrics_track,
                'artist_name': music.get('artist_name')
            }

        return musics
    except:
        return 'Error requesting track list, try again later'