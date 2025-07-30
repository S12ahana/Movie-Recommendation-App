import pickle 
import streamlit as st
import requests

def recommend(movie):
    index=movie[new_df['title']==movie])
st.header("Movie Recommedation system")
movies=pickle.load(open('artifacts/movie_list.pkl','rb'))
similarity=pickle.load(open('artifacts/similarity.pkl','rb'))

movie_list=movies['title'].values
selected_movie=st.selectbox(
    'Type os select a movie to get a recommendation',
    movie_list
    )
if st.button('show recommendation'):
    recommendded_movies_name,  recommended_movies_poster=recommend(selected_movie)