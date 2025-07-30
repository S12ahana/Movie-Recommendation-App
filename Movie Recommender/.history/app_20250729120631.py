import pickle 
import streamlit as st
import requests

st.header("Movie Recommedation system")
movies=pickle.load(open('artifacts/movie_list.pkl','rb'))
similarity=pickle.load(open('artifacts/similarity.pkl','rb'))

movie_list=movies['title'].values
st.selectbox('Type os select  a movie to get a recommendation')