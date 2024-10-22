#Adaptation of another word cloud app

#Import libarary
import streamlit as st
import pandas as pd
#import palmerpenguins
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import string
import numpy as np
from PIL import Image


#streamlit code:
st.title("WordClooud Generator")
user_text_input = st.text_input("Insert text for wordcloud.")


#upload document #change this section of the file
#uploaded_file = 

#"What Happened?",
#"Action Taken (at the time of the incident)",
#"Summary of Actions Taken (Investigation)",
#"Lessons Learned"
uploaded_file = st.file_uploader("Choose a file", type=['csv','xlsx'])
if uploaded_file is not None:
    #read csv
    df=pd.read_csv(uploaded_file)
   #read xls or xlsx
   #df1=pd.read_excel(uploaded_file)
else:
    st.warning("you need to upload a csv or excel file.")

st.text(uploaded_file.name)


uploaded_image_mask = st.file_uploader(
    "Please upload an image file as mask for wordcloud",
    type=["png", "jpg", "jpeg"], key ="2"
    )
if uploaded_image_mask is not None:
    bytes_data = uploaded_image_mask.getvalue()
    # Show the image filename and image.
    st.image(bytes_data)
    st.text(f'filename: {uploaded_image_mask.name}')

    uploaded_image_mask = np.array(Image.open(uploaded_image_mask.name))
#uploaded_image_mask = Image.open(uploaded_image_mask)
#img_array = np.array(uploaded_image_mask)


chosen_specialty = st.selectbox(
    "Choose a Speciality",
    options=df['Speciality'].drop_duplicates().tolist())

chosen_category = st.selectbox(
    "Choose a Category",
    options=df['Category'].drop_duplicates().tolist())

chosen_divsion = st.selectbox(
    "Choose a Division",
    options=df['Division'].drop_duplicates().tolist())


choose_colour = st.selectbox(
   "Choose a colour scheme",
    ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Grays', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_grey', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gist_yerg', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'grey', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']
#    ["Black", "Reds", "Wisteria","BuPu_r"],

)

def create_word_cloud(data_column):
    full_text = ' '.join(data_column)
    full_text = str(full_text)
    #stopwords
    stopwords = set(STOPWORDS)
    stop_words = list(stopwords)
    custom_stop_words = ["movie","film","back","future","one"]
    stop_words = set(stop_words + custom_stop_words)
    #token processing
    tokens = full_text.split()
    punctuation_mapping_table = str.maketrans('', '', string.punctuation)
    tokens_stripped_of_punctuation = [token.translate(punctuation_mapping_table)
                                    for token in tokens]
    lower_tokens = [token.lower() for token in tokens_stripped_of_punctuation]
    joined_string = (" ").join(lower_tokens)
    #image generation
    fig, ax = plt.subplots()
    if uploaded_image_mask is not None:
    
        wordcloud = WordCloud(#font_path = 'font\\GothamMedium.ttf',
                            background_color = 'white',
                            min_word_length =3, 
                            mask = uploaded_image_mask,
                            contour_width = 2,
                            contour_color = 'white',
                            colormap = choose_colour,
        #                      max_words=2000,
        #                      min_font_size=2,
        #                      max_font_size=40,
                            width = 1800,
                            height = 1800).generate(joined_string)
    else:
        wordcloud = WordCloud(#font_path = 'font\\GothamMedium.ttf',
                        background_color = 'white',
                        min_word_length =3, 
                        contour_width = 2,
                        contour_color = 'white',
                        colormap = choose_colour,
    #                      max_words=2000,
    #                      min_font_size=2,
    #                      max_font_size=40,
                        width = 1800,
                        height = 1800).generate(joined_string)
        
    # Turn off axes
    plt.axis("off")
    # Then use imshow to plot an image (here, our wordcloud)
    plt.imshow(wordcloud, interpolation='bilinear') #, interpolation='bilinear' 
    plt.show()
    st.pyplot(fig)

tab1, tab2, tab3, tab4 = st.tabs([
    "What Happened?",
    "Lessons Learned",
    "Actions Taken (during incident)",
    "Summary of Actions Taken (Investigation)",
])
if uploaded_file is not None or user_text_input is not None:
    with tab1:
        create_word_cloud(df['What Happened?'])

        filename1 = 'output/my_word_cloud1.png'
        plt.savefig(filename1)

        with open(filename1, "rb") as img:
            btn = st.download_button(
                label="Download image",
                data=img,
                file_name=filename1,
                mime="image/png"
            )
    with tab2:
        create_word_cloud(df['Lessons Learned'])
        
        filename2 = 'output/my_word_cloud2.png'
        plt.savefig(filename2)

        with open(filename2, "rb") as img:
            btn = st.download_button(
                label="Download image",
                data=img,
                file_name=filename2,
                mime="image/png"
            )
    with tab3:
        create_word_cloud(df['Action Taken (at the time of the incident)'])

        filename3 = 'output/my_word_cloud3.png'
        plt.savefig(filename3)

        with open(filename3, "rb") as img:
            btn = st.download_button(
                label="Download image",
                data=img,
                file_name=filename3,
                mime="image/png"
            )
    with tab4:
        create_word_cloud(df['Summary of Actions Taken (Investigation)'])

        filename4 = 'output/my_word_cloud4.png'
        plt.savefig(filename4)

        with open(filename4, "rb") as img:
            btn = st.download_button(
                label="Download image",
                data=img,
                file_name=filename4,
                mime="image/png"
            )


