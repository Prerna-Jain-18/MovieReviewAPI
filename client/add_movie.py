# add_movie.py
import requests

url = "http://127.0.0.1:5000/movies"
data = {
    "title": "Inception",
    "director": "Christopher Nolan",
    "release_year": 2010
}

# Send POST request to add a new movie
response = requests.post(url, json=data)
print(response.json())
