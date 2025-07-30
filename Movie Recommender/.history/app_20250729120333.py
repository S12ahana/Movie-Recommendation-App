import pickle 
import streamlit as st
import requests

st.header("Movie Recommedation system")
movies=pickle.load('artifacts/movie_list.pkl','')