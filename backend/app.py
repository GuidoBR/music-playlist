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
    request_url = get_request_url("track.search", "q_lyrics", lyrics)
    r = requests.get(request_url)
    if (get_status_code(r) != 200):
        print('Error: {} - {}'.format(get_status_code(r), request_url))
        return ''

    track_list = r.json().get('message').get('body').get('track_list')
    return track_list

def get_lyrics(track_id: int):
    request_url = get_request_url("track.lyrics.get", "track_id", track_id)
    r = requests.get(request_url)

    if (get_status_code(r) != 200):
        print('Error: {} - {}'.format(get_status_code(r), request_url))
        return ''

    return r.json().get('message').get('body').get('lyrics').get('lyrics_body')

def get_status_code(request: dict):
    return request.json().get('message').get('header').get('status_code')

def get_request_url(method_name: string, query: string, query_value: any) -> str:
    prepare_request = {
        'method_name': method_name,
        'format': "json",
        'callback': "callback",
        "api_key": MUSIX_API_KEY,
        "query": query,
        "query_value": query_value
    }
    return "{}{}?format={}&callback={}&apikey={}&{}={}".format(
        BASE_MUSIC_URL,
        prepare_request['method_name'], prepare_request['format'], prepare_request['callback'], prepare_request['api_key'],
        prepare_request['query'], prepare_request['query_value']
    )



