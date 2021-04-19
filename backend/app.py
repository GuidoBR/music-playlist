from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

BASE_MUSIC_URL = "https://api.musixmatch.com/ws/1.1/"
MUSIX_API_KEY = os.environ.get('MUSIX_API_KEY')

@app.route('/track/search/<lyrics>')
def search(lyrics: str) -> str:
    """Fetches music information from a MusixMatch.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by table_handle.  String keys will be UTF-8 encoded.

    Args:
        lyrics: Keywords for search inside music lyrics.

    Returns:
        A json mapping with information for two songs. For example:

        {
            "musics":
            [
                {
                    "artist_name": "AVID All Stars",
                    "lyrics":"All you need is love\nAll you need is love\nAll you need is love, love\nLove is all you need\n,
                    "track_name":"All You Need Is Love (In the Style of the Beatles)",
                    "url":"https://www.musixmatch.com/lyrics/AVID-All-Stars/All-You-Need-Is-Love-In-the-Style-of-the-Beatles?utm_source=application&utm_campaign=api&utm_medium=Draper+AI%3A1409619881554"},
                {
                    "artist_name":"Mardie",
                    "lyrics":"All I need is love (radio Edit 90s)\n\nAll I need is love\nAll I need is love, uh yeah\n\nAll I need is love\n",
                    "track_name":"All I need is love",
                    "url":"https://www.musixmatch.com/lyrics/Mardie/All-I-need-is-love?utm_source=application&utm_campaign=api&utm_medium=Draper+AI%3A1409619881554"
                }
            ]
        }
    """
    musics = {'musics': [get_music_information(lyrics, 0), get_music_information(lyrics, 1)]}

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

def get_request_url(method_name: str, query: str, query_value: any) -> str:
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



