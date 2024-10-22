"""
HSMA Group 6 - Hackathon 2, 22/10/2024

1. Set up GitHub x
2. Create ignore data file + read.me file x
2.1 Create Environment x
3. Data load
4. Explore data,
5. Data Pre-processing
6. Creating features and scripting for overall information, + NLP, streamlit as 
    the output for interaction with end user.
7. Create Streamlit front-end interface.
8. SPC from py.plot.dot?

"""
# %%
# 1. Import packages
#Dataframe tools
import pandas as pd
import numpy as np

#Preprocessing of datetimes
from datetime import datetime

#Data Visualisation
import plotly.express as px
import matplotlib.pyplot as plt

# NLP tools
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
### SpaCy NLTK for NER
#import en_core_web_sm
# pip install spacy == 3.2.0
# python -m spacy download en_core_web_sm

# for numpy but with images
from PIL import Image

#
# %%
#import the data file
datix_df = pd.read_csv("data\Test_data.csv")

# %%
datix_df.head(5)

# %%
#Check for columns 
datix_headers = datix_df.columns

# %%
# Data pre-processing
# Changing Actual Harm category to numerical values
try: 
    datix_df["Actual_Harm_ord"] = datix_df["Actual Harm"]
    datix_df["Actual_Harm_ord"] = datix_df["Actual_Harm_ord"].replace("None (No harm)", 0)
    datix_df["Actual_Harm_ord"] = datix_df["Actual_Harm_ord"].replace("Low (Minimal harm: required extra observation or minor treatment)", 1)
    datix_df["Actual_Harm_ord"] = datix_df["Actual_Harm_ord"].replace("Moderate (Short-term harm: required further treatment or procedure)", 2)
    datix_df["Actual_Harm_ord"] = datix_df["Actual_Harm_ord"].replace("Severe\xa0(Permanent or long-term harm: e.g. fractured NOF)", 3)
    datix_df["Actual_Harm_ord"] = datix_df["Actual_Harm_ord"].replace("Death (Not caused by a safety incident)", 4)
    datix_df["Actual_Harm_ord"] = datix_df["Actual_Harm_ord"].replace("Death\xa0(Caused by a safety incident)", 5)
except:
    print("Data modification for 'Actual Harms' already completed.")
    pass

datix_df["Division"].columns
datix_df["Specialty"].columns
datix_df["Category"].columns
datix_df["Sub Category"].columns



# %%
