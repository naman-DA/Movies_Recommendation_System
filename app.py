import streamlit as st
import pickle
import requests
import os

API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3/movie/"
SIMILARITY_FILE = "similarity.pkl"
MODEL_URL = "https://github.com/naman-DA/Movies_Recommendation_System/releases/download/v1.0/similarity.pkl"

@st.cache_resource
def load_similarity():
    if not os.path.exists(SIMILARITY_FILE):
        with st.spinner("Downloading recommendation model..."):
            r = requests.get(MODEL_URL, stream=True, timeout=60)
            r.raise_for_status()
            with open(SIMILARITY_FILE, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

    with open(SIMILARITY_FILE, "rb") as f:
        return pickle.load(f)

similarity = load_similarity()

@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    try:
        response = requests.get(
            f"{BASE_URL}{movie_id}",
            params={
                "api_key": API_KEY,
                "language": "en-US"
            },
            timeout=5
        )
        response.raise_for_status()
        data = response.json()

        poster_path = data.get("poster_path")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path
        else:
            return "https://via.placeholder.com/300x450?text=No+Poster"

    except Exception as e:
        return "https://via.placeholder.com/300x450?text=Error"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters

movies = pickle.load(open('movies.pkl', 'rb'))
st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    'How will you predict a movie',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)

    for col, name, poster in zip(cols, names, posters):
        with col:
            st.image(poster, use_container_width=True)
            st.markdown(f"**{name}**")
