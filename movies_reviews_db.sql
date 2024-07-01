CREATE DATABASE movie_review_db;

USE movie_review_db;

CREATE TABLE movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    director VARCHAR(255),
    release_year INT
);

CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    review_text TEXT,
    rating INT,
    FOREIGN KEY (movie_id) REFERENCES movies(id)
);


Select * from movies;
Select * from reviews;
