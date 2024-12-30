from flask import Flask, request, render_template, redirect
import pandas as pd

app = Flask(__name__)

# Define the movie data
data = {
    'Title': ['Inception', 'The Dark Knight', 'Interstellar', 'Parasite', 'The Matrix'],
    'Genre': ['Sci-Fi, Thriller', 'Action, Crime, Drama', 'Adventure, Drama, Sci-Fi', 'Comedy, Drama, Thriller', 'Sci-Fi, Action']
}

# Create a DataFrame
df = pd.DataFrame(data)

@app.route('/')
def home():
    return redirect('/movies')

@app.route('/movies')
def index():
    return render_template('Iyad.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    genre = request.form['genre']
    filtered_movies = df[df['Genre'].str.contains(genre, case=False, na=False)]
    
    movie_titles = filtered_movies['Title'].tolist()
    
    return render_template('Iyad.html', movies=movie_titles)

@app.route('/all_movies')
def all_movies():
    movie_titles = df['Title'].tolist()
    return render_template('Iyad.html', movies=movie_titles)

if __name__ == '__main__':
    app.run(debug=True)
