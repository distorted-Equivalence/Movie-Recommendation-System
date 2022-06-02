import streamlit as st
import pickle
import pandas as pd
import requests


def poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=07e1ed5f1f35c3821a3191fd5e920e7c&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']



def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    reccom=[]
    posteri=[]
    
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id 



        reccom.append(movies.iloc[i[0]].title)
        posteri.append(poster(movie_id))

    return reccom,posteri 



movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommender System")

option = st.selectbox(
     'How would you like to be contacted?',
     movies['title'].values)

if st.button('Recommend'):

    r,p=recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(r[0])
        st.image(p[0])
    with col2:
        st.text(r[1])
        st.image(p[1])

    with col3:
        st.text(r[2])
        st.image(p[2])
    with col4:
        st.text(r[3])
        st.image(p[3])
    with col5:
        st.text(r[4])
        st.image(p[4])







