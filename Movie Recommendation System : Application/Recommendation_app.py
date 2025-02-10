import pandas as pd
import numpy as np
import kagglehub
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def download_dataset():
    # Download latest dataset from KaggleHub
    path = kagglehub.dataset_download("parasharmanas/movie-recommendation-system")
    print("Path to dataset files:", path)
    
    # List all files in the directory
    print(os.listdir(path))
    
    return path

# Download dataset
path = download_dataset()

# Assuming the dataset files
movies_path = os.path.join(path, 'movies.csv')
ratings_path = os.path.join(path, 'ratings.csv')

def load_data():
    # Load the movies and ratings dataset
    movies = pd.read_csv(movies_path, skiprows=[1])
    ratings = pd.read_csv(ratings_path, skiprows=[1])
    
    # Compute average rating for each movie
    movie_ratings = ratings.groupby("movieId")["rating"].mean().round(1).reset_index()  # Round ratings to 1 decimal place
    movies = movies.merge(movie_ratings, on="movieId", how="left")
    return movies

# Load data
movies = load_data()

# Initialize a TF-IDF Vectorizer on the 'title' column
tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 2))
tfidf_matrix = tfidf_vectorizer.fit_transform(movies["title"])

# Function to find similar movies
def search(title):
    query_vector = tfidf_vectorizer.transform([title])  # Transform input title
    similarity = cosine_similarity(query_vector, tfidf_matrix).flatten()  # Compute similarity
    indices = np.argpartition(similarity, -5)[-5:]  # Get indices of top 5 similar movies
    results = movies.iloc[indices].iloc[::-1]  # Retrieve movie details in descending order of similarity
    return results[["movieId", "title", "genres","rating"]]  # Include genres and ratings in the output

if __name__ == "__main__":
    title = input("Enter movie title: ")
    results = search(title)
    print("\nRecommended Movies:")
    print(results)
