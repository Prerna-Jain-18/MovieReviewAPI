# get_movies.py
import requests

url = "http://127.0.0.1:5000/movies"

# Send GET request to retrieve all movies
response = requests.get(url)
print(response.json())
