import pickle 
import streamlit as st
import requests

def recommend(movie):
    index=movie[movies['title']==movie].index[0]
    distances=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])
    recommended_movies_name=[]
    recommended_movies_poster=[]
    for i in distances[1:6]:
        movie_id=movies.iloc[i[0]]['movie_id']
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_poster.append(movies.iloc[i[0]].title)
    return     recommended_movies_name,recommended_movies_poster
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