import pickle
import streamlit as st

# CSS for styling
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

movies = pickle.load(open('movies_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))


movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Choose a movie to get recommendations:",
    movie_list
)


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
