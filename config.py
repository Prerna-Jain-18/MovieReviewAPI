# config.py
# Database configuration details
import os

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'your_password')    # Change with your database password, replace 'your_password' with your actual password
DB_NAME = os.getenv('DB_NAME', 'movie_review_db')
