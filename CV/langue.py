import streamlit as st
import pandas as pd
import altair as alt

langues = ['Français', 'Anglais', 'Espagnol']
levels = [4, 4, 3]
colors = ['#FF5733', '#90FF33', '#5733FF']  # Define colors for each language

data = pd.DataFrame({'Langue': langues, 'Niveau': levels, 'Color': colors})

def display_language_skills():
    # Create the chart with color encoding
    chart = alt.Chart(data).mark_bar().encode(
        x='Niveau',
        y='Langue',
        color=alt.Color('Color:N', legend=None)  # Color encoding based on 'Color' column
    ).properties(
        width=200,
        height=400,
    )

    # Display the chart with a title
    st.altair_chart(chart, use_container_width=True)

if __name__ == "__main__":
    display_language_skills()

