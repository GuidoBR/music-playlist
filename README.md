# Music API Example

## Backend - Install and run

```
pip install -r requirements.txt
export FLASK_APP=app.py
export MUSIX_API_KEY=<API_KEY>
cd backend
flask run
```

## Frontend - run

```
python -m http.server
```

## Example requests
```
curl -s 127.0.0.1:5000/track/search/despacito
curl -s 127.0.0.1:500/track/search/garota%20de%20ipanema
```
## More information on the external API

https://playground.musixmatch.com/