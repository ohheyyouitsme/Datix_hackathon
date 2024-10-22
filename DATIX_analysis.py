"""
HSMA Group 6 - Hackathon 2, 22/10/2024

1. Set up GitHub x
2. Create ignore data file + read.me file x
2.1 Create Environment x
3. Data load
4. Explore data,
5. Data Pre-processing
6. Creating features and scripting for overall information, + NLP, streamlit as the output for interaction with end user.
7. Create Streamlit front-end interface.
8. SPC from py.plot.dot?

"""
# %%
# 1. Import packages
import pandas as pd
import numpy as np
import plotly.express as px

#
# %%
#import the data file
datix_df = pd.read_csv("data\Test_data.csv")
# %%
datix_df.head(5)

# %%
#Check for columns 
datix_headers = datix_df.columns