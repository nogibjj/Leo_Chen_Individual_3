import psycopg2
from flask import Blueprint, jsonify, request, current_app
from datetime import datetime
import ast
analysis_bp = Blueprint('analysis', __name__, url_prefix='/analysis')

# ！！！！！db info need to be encrypted
conn_params = {
    "dbname": "postgres",
    "user": "ids706",
    "password": "!Qq123456",
    "host": "ids706.postgres.database.azure.com",
    "port": "5432"
}


def get_movie_data(start_year, end_year):

    try:
        conn = psycopg2.connect(**conn_params)
        cursor = conn.cursor()
        current_app.logger.info("Successfully connected to the database.")
    except psycopg2.Error as e:
        current_app.logger.error("Failed to connect to the database: %s", e)
        return jsonify({"error": "Database connection failed"}), 500

    query = """
    SELECT EXTRACT(YEAR FROM release_date) AS year, genres, COUNT(*) as movie_count
    FROM movie
    WHERE EXTRACT(YEAR FROM release_date) BETWEEN %s AND %s
    GROUP BY year, genres
    ORDER BY year, genres;
    """
    # current_app.logger.info("Executing query: %s with start_year=%s, end_year=%s", query, start_year, end_year)
    cursor.execute(query, (start_year, end_year))
    results = cursor.fetchall()

    # current_app.logger.info("Query results: %s", results)
    movie_data = {}
    for year, genres_str, movie_count in results:
        genres = ast.literal_eval(genres_str)

        if year not in movie_data:
            movie_data[year] = {}

        for genre in genres:
            if genre not in movie_data[year]:
                movie_data[year][genre] = 0
            movie_data[year][genre] += movie_count

    # current_app.logger.info("Processed movie data: %s", movie_data)
    cursor.close()
    conn.close()

    return movie_data


@analysis_bp.route('/health')
def health_check():
    return '', 200


@analysis_bp.route('/analyze', methods=['POST'])
def analyze_data():
    data = request.get_json()
    start_year = data.get('startYear')
    end_year = data.get('endYear')

    if not start_year or not end_year:
        return jsonify({"error": "Start year and end year are required"}), 400

    try:
        start_year = int(start_year)
        end_year = int(end_year)

        if start_year > end_year:
            return jsonify({"error": "Start year cannot be greater than end year"}), 404

        movie_data = get_movie_data(start_year, end_year)

        if not movie_data:
            return jsonify({"error": "No data found for the specified years"}), 404

        current_app.logger.info("movie_data: %s", movie_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    response_data = {
        "years": list(range(start_year, end_year + 1)),
        "genres": []
    }

    genre_counts = {}
    for year in response_data["years"]:
        year_data = movie_data.get(year, {})
        for genre, movie_count in year_data.items():
            if genre not in genre_counts:
                genre_counts[genre] = [0] * len(response_data["years"])
            genre_counts[genre][year - start_year] = movie_count

    for genre, counts in genre_counts.items():
        response_data["genres"].append({
            "name": genre,
            "counts": counts
        })
    current_app.logger.info("response: %s", response_data)
    return jsonify(response_data), 200


# api for analyze movie popularity
@analysis_bp.route('/popularity', methods=['POST'])
def analyze_popularity():
    data = request.get_json()
    year = data.get('year')

    if not year:
        return jsonify({"error": "Year is required"}), 400

    try:
        year = int(year)
        conn = psycopg2.connect(**conn_params)
        current_app.logger.info("response: %s", year)
        cursor = conn.cursor()
        query = """
        SELECT title, popularity
        FROM movie
        WHERE EXTRACT(YEAR FROM release_date) = %s
        ORDER BY popularity DESC;
        """
        cursor.execute(query, (year,))
        results = cursor.fetchall()
        cursor.close()
        conn.close()

        if not results:
            return jsonify({"error": "No movies found for the specified year"}), 404

        # Get top 5 and bottom 5 movies
        top_movies = results[:5]
        bottom_movies = results[-5:]

        response_data = {
            "top_movies": [{"title": title, "popularity": popularity} for title, popularity in top_movies],
            "bottom_movies": [{"title": title, "popularity": popularity} for title, popularity in bottom_movies]
        }
        current_app.logger.info("response: %s", response_data)
        return jsonify(response_data), 200

    except Exception as e:
        current_app.logger.error("Error analyzing popularity: %s", e)
        return jsonify({"error": str(e)}), 500
