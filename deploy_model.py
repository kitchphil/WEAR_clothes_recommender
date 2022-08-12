# Python libraries
import streamlit as st
from PIL import Image
import html
# User module files
from userinput import userinput
from clothesrecommender import clothesrecommender
from test import userinput

def main():

    #############
    # Main page #
    #############

    options = ['Home','Recommender','Stop']
    choice = st.sidebar.selectbox("Menu",options, key = '1')

    if ( choice == 'Home' ):
        st.markdown("<h1 style='text-align: center; color: black;'>WEAR</h1>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: gray;'>Weather Engineered Apparel Recommender</h4>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write('', width = 2)

        with col2:
            st.image("./images/cloud-rain-and-sun-icon-Graphics-1-1-580x386.jpeg", width = 400, use_column_width = 'auto')

        with col3:
            st.write('', width = 2)
        st.markdown("<h3 style='text-align: center; color: black;'>never leave home unprepared again</h3>", unsafe_allow_html=True)
        pass

    elif ( choice == 'Recommender' ):
        userinput()
        pass

    else:
        st.stop()


main()