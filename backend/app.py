from flask import Flask, jsonify
import requests
import random
import os
import string

app = Flask(__name__)

BASE_MUSIC_URL = "https://api.musixmatch.com/ws/1.1/"
MUSIX_API_KEY = os.environ.get('MUSIX_API_KEY')

@app.route('/track/search/<lyrics>')
def search(lyrics: str) -> str:
    musics = {'musics': []}

    musics['musics'].append(get_music_information(lyrics, 0))
    musics['musics'].append(get_music_information(lyrics, 1))

    response = jsonify(musics)
    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

def get_music_information(lyrics: str, position: int):
    track_list = get_tracks(lyrics)
    music = track_list[position].get('track')

    return {
        'track_name': music.get('track_name'),
        'lyrics': get_lyrics(music.get('track_id')),
        'artist_name': music.get('artist_name'),
        'url': music.get('track_share_url')
    }

def get_tracks(lyrics: str):
    try:
        base_request = "track.search?format=json&callback=callback&quorum_factor=1&apikey={}&q_lyrics=".format(MUSIX_API_KEY)
        music_request = "{}{}{}".format(BASE_MUSIC_URL, base_request, lyrics)
        r = requests.get(music_request)
        track_list = r.json().get('message').get('body').get('track_list')

        return track_list
    except:
        return 'Error requesting track list, try again later'

def get_lyrics(track_id: int):
    request = {
        'name': "track.lyrics.get",
        'format': "json",
        'callback': "callback",
        "quorum_factor": 1,
        "api_key": MUSIX_API_KEY,
        "query": "track_id",
        "query_value": track_id
    }
    request_url = "{}{}?format={}&callback={}&apikey={}&{}={}".format(
        BASE_MUSIC_URL,
        request['name'], request['format'], request['callback'], request['api_key'],
        request['query'], request['query_value']
    )

    r = requests.get(request_url)

    if (get_status_code(r) != 200):
        print('Error getting lyrics - {} - {}'.format(get_status_code(r), request_url))
        return ''

    return r.json().get('message').get('body').get('lyrics').get('lyrics_body')

def get_status_code(request):
    return request.json().get('message').get('header').get('status_code')



