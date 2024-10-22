import pandas as pd
import streamlit as st
import time


# initiate session states
if 'selected_divisions' not in st.session_state:
    st.session_state.selected_divisions = None

if 'selected_specialties' not in st.session_state:
    st.session_state.selected_specialties = None

# load main df
datix_df = pd.read_csv("../data/1924_Total.csv")

# select division
selected_divisions = st.multiselect(
    "Select division(s)",
    datix_df["Division"].drop_duplicates().sort_values().tolist(),
    default=st.session_state.selected_divisions
)

# filter on division
edited_df = datix_df[datix_df["Division"].isin(selected_divisions)]

# select specialty
selected_specialties = st.multiselect(
    "Select specialty(s)",
    edited_df["Speciality"].drop_duplicates().sort_values().tolist(),
    default=st.session_state.selected_specialties
)

# filter on specialties
edited_df = datix_df[datix_df["Speciality"].isin(selected_specialties)]

# set session states
st.session_state.selected_divisions = selected_divisions
st.session_state.selected_specialties = selected_specialties

with st.spinner(text="In progress"):
    time.sleep(2)

## dataframe
st.dataframe(
    # Pass edited df
    edited_df[[ 'Category',
    'Sub Category',
    'Result',
    'Actual Harm',
    'Incident Date',
    'Time of Incident',
    'Reported Date',
    'Division',
    'Speciality',
    'Location (Exact)',
    'What Happened?',
    'Action Taken (at the time of the incident)',
    'Summary of Actions Taken (Investigation)',
    'Lessons Learned',
    'Approved Date'
    ]],
    # This means it will take up the maximum possible width
    # (here, the full width of the column)
    use_container_width=True,
    # This hides the index column, which isn't really necessary in this dataframe
    hide_index=True
    )
