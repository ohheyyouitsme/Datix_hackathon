import streamlit as st

st.write("Here's the simulation map and calculation")

if 'iat_calls' not in st.session_state:
    st.session_state.iat_calls = None 
if 'iat_walkins' not in st.session_state:
    st.session_state.iat_walkins = None

if st.session_state.iat_calls is None:
    st.write("There is no average time because the model has not yet run")
else:
    st.write(f"The IAT calls number is {st.session_state.iat_calls:.1f}")

if st.session_state.iat_walkins is None:
    st.write("There is no walkins average because the model has not yet run")
else:
    st.write(f"The IAT walkins number is {st.session_state.iat_walkins:.1f}")