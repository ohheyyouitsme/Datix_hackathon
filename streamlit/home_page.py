import streamlit as st

st.title("Overview of analysis of the Trust's Datix incident data")
st.write("Welcome to the Datix EDA Project! This project is all about exploring and analysing healthcare incident reporting data (Datix).", 
         "Our aim is to uncover trends, visualise insights, and apply Natural Language Processing (NLP) to better understand the narrative behind incident reports.")


# example code for setting session states, in case it is needed
# if 'iat_calls' not in st.session_state:
#     st.session_state.iat_calls = None 
# if 'iat_walkins' not in st.session_state:
#     st.session_state.iat_walkins = None