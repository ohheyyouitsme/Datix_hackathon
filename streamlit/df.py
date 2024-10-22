import pandas as pd
import streamlit as st

datix_df = pd.read_csv(r"..\data\1924_Total.csv")

## dataframe
st.dataframe(
    # We pass in the dataframe but limit it to these 5 columns
    datix_df[[ 'Category',
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
