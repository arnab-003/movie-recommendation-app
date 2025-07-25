import streamlit as st
import pickle
import os
import gdown

# ---------- Download files from Google Drive if not present ----------
def download_file_from_drive(file_id, output_path):
    if not os.path.exists(output_path):
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, output_path, quiet=False)
        print(f"✅ Downloaded {output_path}")

# Google Drive file IDs
MOVIES_ID = '1hP9MfYV3_MRZynUVcWvzHa4itEFQHQo_'
SIMILARITY_ID = '1fVhAgloprV_RGg6SgPuZYvX5Wh3f3JeR'

# Download if files not available locally
download_file_from_drive(MOVIES_ID, 'movies_list.pkl')
download_file_from_drive(SIMILARITY_ID, 'similarity.pkl')

# ---------- Load the data ----------
with open('movies_list.pkl', 'rb') as f:
    movies = pickle.load(f)

with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

# ---------- Streamlit UI ----------
st.markdown("""
    <style>
        .header {
            text-align: center;
            color: #1E90FF;
            font-size: 36px;
            font-weight: bold;
            margin-top: 30px;
        }
        .subheader {
            text-align: center;
            color: #32CD32;
            font-size: 24px;
            margin-top: 20px;
        }
        .movie-name {
            font-size: 18px;
            color: #ff6347;
            text-align: center;
            font-weight: bold;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        .movie-name:hover {
            color: #ff4500;
            transform: scale(1.1);
        }
        .movie-card {
            background-color: #f0f8ff;
            border: 1px solid #dcdcdc;
            border-radius: 10px;
            padding: 10px;
            margin: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }
        .movie-card:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
        }
        .button-style {
            background-color: #ff6347;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px 20px;
            border: none;
        }
        .button-style:hover {
            background-color: #ff4500;
        }
    </style>
""", unsafe_allow_html=True)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names

st.markdown('<div class="header">🎬 Movie Recommender System</div>', unsafe_allow_html=True)

movie_list = movies['title'].values
selected_movie = st.selectbox("Choose a movie to get recommendations:", movie_list)

if st.button('Show Recommendations', key="recommendations", help="Click to get movie recommendations", use_container_width=True):
    recommended_movie_names = recommend(selected_movie)
    st.markdown('<div class="subheader">Here are some Movie Recommendations for you:</div>', unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown(f'<div class="movie-card"><p class="movie-name">{recommended_movie_names[0]}</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="movie-card"><p class="movie-name">{recommended_movie_names[1]}</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="movie-card"><p class="movie-name">{recommended_movie_names[2]}</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown(f'<div class="movie-card"><p class="movie-name">{recommended_movie_names[3]}</p></div>', unsafe_allow_html=True)
    with col5:
        st.markdown(f'<div class="movie-card"><p class="movie-name">{recommended_movie_names[4]}</p></div>', unsafe_allow_html=True)
