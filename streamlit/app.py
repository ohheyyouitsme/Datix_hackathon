import streamlit as st

pg = st.navigation([
    st.Page("home_page.py", title="Welcome!"),
    st.Page("df.py", title="Summary table of incidents"),
    st.Page("eda.py", title = "Graphs..."),
    st.Page("datix_wordcloud_app.py", title = "Wordclouds...")
])

#st.logo("hsma_logo.png")

pg.run()