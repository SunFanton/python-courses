from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import difflib

# Cargar los datos de películas y la matriz de similitud
movies_data = pd.read_csv('../data/movies.csv')  # Asegúrate de que este archivo exista
similarity = np.load('movies_similarity_matrix.npy')
all_movies_names_list = movies_data["title"].tolist()
max_movies_recommendations = 10

app = Flask(__name__)

@app.route('/recommend', methods=['GET'])
def recommend():
    movie_name = request.args.get('movie_name', default='', type=str)
    
    if not movie_name:
        return jsonify({"error": "No movie name provided"}), 400

    find_close_match = difflib.get_close_matches(movie_name, all_movies_names_list)
    
    close_match = find_close_match[0] if len(find_close_match) > 0 else "N/A"
    
    if close_match == "N/A":
        return jsonify({"error": "No close match found"}), 404

    movie_index = movies_data[movies_data["title"] == close_match]["index"].values[0]
    similarity_score = list(enumerate(similarity[movie_index]))
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    recommended_movies = []

    for idx, cosine in sorted_similar_movies[0:max_movies_recommendations]:
        movie = movies_data[movies_data["index"] == idx]["title"].values[0]
        recommended_movies.append(movie)

    return jsonify({"recommended_movies": recommended_movies})

if __name__ == '__main__':
    app.run(debug=True)