import streamlit as st

def set_background_color():
    st.markdown(
        """
        <style>
        body {
            background-color: #DE2525;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

