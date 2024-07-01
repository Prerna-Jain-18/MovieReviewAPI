# add_review.py
import requests

url = "http://127.0.0.1:5000/reviews"
data = {
    "movie_id": 1,
    "review_text": "Amazing movie with mind-bending plot!",
    "rating": 5
}

# Send POST request to add a new review
response = requests.post(url, json=data)
print(response.json())
