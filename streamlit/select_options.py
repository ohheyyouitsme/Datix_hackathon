import streamlit as st
import pandas as pd

# load main df
datix_df = pd.read_csv("../data/Test_data.csv")

# select division
selected_divisions = st.multiselect(
    "Select division(s)",
    datix_df["Division"].drop_duplicates().sort_values().tolist()
)

# filter on division
edited_df = datix_df[datix_df["Division"].isin(selected_divisions)]

# select specialty
selected_specialties = st.multiselect(
    "Select specialty(s)",
    edited_df["Speciality"].drop_duplicates().sort_values().tolist()
)

# filter on specialties
edited_df = datix_df[datix_df["Speciality"].isin(selected_specialties)]


# datix_df["Category"].columns
# datix_df["Sub Category"].columns