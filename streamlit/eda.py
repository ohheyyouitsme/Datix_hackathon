import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
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
    # We can then specify configurations for some or all of the columns
    # to refine how they get displayed
    # This is a dictionary with the original column name on the left
    # and each column separated by commas
    # If we just provide a string on the right of the :, then this will just change the
    # name that is displayed in the column header
    # If we provide a st.column_config then we can select from a range
    # of column types detailed in the Streamlit documentation
    # column_config={
    #     "Series_Title": "Title",
    #     "IMDB_Rating": "Rating",
    #     "Released_Year":st.column_config.NumberColumn(
    #         "Released In", # Change the title displayed
    #         format="%d" # Format it as digits with no comma in
    #         ),
    #     "Runtime":"Runtime (Minutes)"
# }
    )


harm_by_category = datix_df.groupby(['Category', 'Actual Harm']).size().unstack()

plt.figure(figsize=(12, 8))
harm_by_category.plot(kind='bar', stacked=True, figsize=(12, 8))
plt.title('Harm Types Per Category')
plt.xlabel('Category')
plt.ylabel('Number of Incidents')
plt.xticks(rotation=45)
plt.legend(title="Harm Type (Actual Harm)", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


# st.set_page_config(layout="wide")
# col1, col2 = st.columns(2)
# st.title('Harm types per category')