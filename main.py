from flask import Flask, request, jsonify, send_from_directory
from db_utils import execute_query
import os

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'index.html')


@app.route('/movies', methods=['GET'])
def get_movies():
    query = "SELECT * FROM movies"
    try:
        cursor = execute_query(query)
        movies = cursor.fetchall() if cursor else []
        print(f"Movies fetched: {movies}")
        return jsonify(movies)
    except Exception as e:
        print(f"Error fetching movies: {e}")
        return jsonify({'error': str(e)}), 500

# Route to add a new movie
@app.route('/movies', methods=['POST'])
def add_movie():
    data = request.get_json()
    query = "INSERT INTO movies (title, director, release_year) VALUES (%s, %s, %s)"
    cursor = execute_query(query, (data['title'], data['director'], data['release_year']))
    if cursor:
        return jsonify({'message': 'Movie added successfully'}), 201
    else:
        return jsonify({'message': 'Failed to add movie'}), 500

# Route to get a specific movie by ID
@app.route('/movies/<int:id>', methods=['GET'])
def get_movie(id):
    query = "SELECT * FROM movies WHERE id = %s"
    try:
        cursor = execute_query(query, (id,))
        movie = cursor.fetchone() if cursor else None
        print(f"Movie fetched: {movie}")
        return jsonify(movie)
    except Exception as e:
        print(f"Error fetching movie: {e}")
        return jsonify({'error': str(e)}), 500

# Route to get all reviews
@app.route('/reviews', methods=['GET'])
def get_reviews():
    query = "SELECT * FROM reviews"
    try:
        cursor = execute_query(query)
        reviews = cursor.fetchall() if cursor else []
        print(f"Reviews fetched: {reviews}")
        return jsonify(reviews)
    except Exception as e:
        print(f"Error fetching reviews: {e}")
        return jsonify({'error': str(e)}), 500

# Route to get a specific review by ID
@app.route('/reviews/<int:id>', methods=['GET'])
def get_review(id):
    query = "SELECT * FROM reviews WHERE id = %s"
    try:
        cursor = execute_query(query, (id,))
        review = cursor.fetchone() if cursor else None
        print(f"Review fetched: {review}")
        return jsonify(review)
    except Exception as e:
        print(f"Error fetching review: {e}")
        return jsonify({'error': str(e)}), 500

# Route to add a new review for a movie
@app.route('/reviews', methods=['POST'])
def add_review():
    data = request.get_json()
    query = "INSERT INTO reviews (movie_id, review_text, rating) VALUES (%s, %s, %s)"
    cursor = execute_query(query, (data['movie_id'], data['review_text'], data['rating']))
    if cursor:
        return jsonify({'message': 'Review added successfully'}), 201
    else:
        return jsonify({'message': 'Failed to add review'}), 500

#Run the flask app
if __name__ == '__main__':
    app.run(debug=True)
