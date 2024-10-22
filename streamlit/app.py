import streamlit as st

pg = st.navigation([
    st.Page("home_page.py", title="Welcome!"),
    st.Page("des_page.py", title="Run Simulation"),
    st.Page("lsoa_map.py", title = "LSOA")
])

st.logo("hsma_logo.png")

pg.run()