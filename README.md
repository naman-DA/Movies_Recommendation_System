# Movies_Recommendation_System

A **content-based movie recommendation system** built with Machine Learning and deployed as a **production-ready web application** using Streamlit and Render.

The system recommends similar movies based on metadata similarity and displays posters using the TMDB API.

---

## Live Demo

🔗 https://movies-recommendation-system-64hb.onrender.com

---

## Features

- Content-based movie recommendations using **cosine similarity**
- Interactive **Streamlit web interface**
- Dynamic movie poster fetching using **TMDB API**
- Large ML model handled via **GitHub Releases**
- Secure API key handling using **environment variables**
- Optimized with caching for faster performance

---

## How It Works

1. Movie metadata (genres, overview, keywords) is preprocessed.
2. Text data is vectorized and cosine similarity is computed.
3. When a user selects a movie:
   - The system finds the most similar movies.
   - Top recommendations are displayed with posters.

---

## Tech Stack

- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn  
- **Web Framework:** Streamlit  
- **Deployment:** Render  
- **Model Hosting:** GitHub Releases  
- **External API:** TMDB API  

---

## Project Structure

├── app.py # Streamlit application
├── requirements.txt # Dependencies
├── movies.pkl # Movie metadata
├── similarity.pkl # Similarity matrix (hosted via GitHub Release)
├── similarity.pkl # Similarity matrix (hosted via GitHub Release)

> Note: `similarity.pkl` is **not stored in the repository** due to GitHub’s size limit.  
> It is downloaded dynamically from a GitHub Release at runtime.

---

## Environment Variables

Create the following environment variable in Render:
TMDB_API_KEY=your_tmdb_api_key


The API key is **not hardcoded** in the source code for security reasons.

---

## Model Handling (Important)

- The similarity matrix (`similarity.pkl`) is larger than 100 MB.
- It is hosted as a **GitHub Release asset**.
- The application downloads and caches the model at runtime.

This approach avoids GitHub size limits and follows real-world ML deployment practices.
