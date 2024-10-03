import streamlit as st
import pickle


st.header("Movies Recomendation System")

movie = pickle.load(open("C:\\Users\\ASUS\\OneDrive\\Desktop\\streamlit_dashboards\\Model\\movies_list.pkl","rb"))
similarty = pickle(load(open("C:\\Users\\ASUS\\OneDrive\\Desktop\\streamlit_dashboards\\Model\\similarity.pkl","rb")))


movie_list = movie("title").values

st.selectbox(
    "type movie name",
    movie_list
)