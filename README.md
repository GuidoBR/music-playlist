# Music API Example

![music-app](/home/guido/Projects/music-playlist/music-app.gif)

## Backend - Install and run

```
pip install -r requirements.txt
export FLASK_APP=app.py
export MUSIX_API_KEY=<API_KEY>
cd backend
flask run
```

### Tests

```
python backend/test_app.py
```

## Frontend - run

```
python -m http.server
```

## Example requests
```
curl -s 127.0.0.1:5000/track/search/despacito
curl -s 127.0.0.1:5000/track/search/garota%20de%20ipanema
```
## More information on the external API

[MusixMatch](https://playground.musixmatch.com/)
