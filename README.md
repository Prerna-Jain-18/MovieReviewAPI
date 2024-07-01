# Movie Review API

This project is a simple Movie Review API built using Flask and MySQL. It demonstrates basic CRUD operations and allows users to add new movies, retrieve movie lists, and submit reviews for movies.

## Features

- **Add a New Movie**: Allows users to add a movie by providing the title, director, and release year.
- **Get All Movies**: Retrieves a list of all movies stored in the database.
- **Get a Specific Movie**: Retrieves the details of a specific movie by its ID.
- **Add a Review**: Allows users to add a review for a movie by providing the movie ID, review text, and rating.

## Installation

### Prerequisites

- Python 3.10.5
- MySQL database
- Flask
- PyMySQL
- Requests library

### Setup Steps

1. **Clone the Repository**: Clone the repository to your local machine.

2. **Create a Virtual Environment**: Set up a virtual environment and activate it.

3. **Install Dependencies**: Install all the required dependencies listed in the `requirements.txt` file.

4. **Set Up MySQL Database**: Create the necessary database and tables in MySQL.

5. **Configure Database Connection**: Create a configuration file for your MySQL database credentials.

6. **Run the Application**: Start the Flask application.

## API Endpoints

### Add a New Movie

- **Endpoint**: `/movies`
- **Method**: POST
- **Description**: Adds a new movie to the database.
- **Request Body**: Requires the title, director, and release year of the movie.

### Get All Movies

- **Endpoint**: `/movies`
- **Method**: GET
- **Description**: Retrieves all movies from the database.

### Get a Specific Movie

- **Endpoint**: `/movies/<id>`
- **Method**: GET
- **Description**: Retrieves a specific movie by its ID.

### Add a Review

- **Endpoint**: `/reviews`
- **Method**: POST
- **Description**: Adds a review for a movie.
- **Request Body**: Requires the movie ID, review text, and rating.

## Usage

You can interact with the API using tools like Postman. For example, to add a new movie, you would create a POST request to the `/movies` endpoint with the required movie information in the request body.

## Testing

Use Postman to manually test the API endpoints. Follow these steps:

1. **Open Postman**.
2. **Create a New Request**: Choose the HTTP method and enter the API endpoint URL.
3. **Set Up the Request Body**: For POST requests, specify the JSON data in the request body.
4. **Send the Request**: Click the "Send" button and observe the response.

