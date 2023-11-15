from pathlib import Path

import streamlit as st
from PIL import Image
from langue import display_language_skills
import folium
from map import display_map
import numpy as np
from color import set_background_color
import os

# Def des infos
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
profile_pic_path = current_dir /"Annexe" /"Pedobear.jpg"
fichierpdf = current_dir / "Annexe" /"test.pdf"
PAGE_TITLE = 'CV | Guillaume Dorges'
PAGE_ICON = ':partying_face::partying_face:'
NAME = 'Guillaume Dorges'
DESCRIPTION = """
RECONVERSION EN INFORMATIQUE
"""
EMAIL = "dorges.guillaume@gmail.com"
SOCIAL_MEDIA_URL = 'http://github.com/MaoenD'

try:
    with open(fichierpdf, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
except FileNotFoundError:
    st.error("PDF file not found.")
except Exception as e:
    st.error(f"An error occurred: {e}")
    PDFbyte = None


# config page streamlit
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

#config page background
set_background_color()

# image + infos
st.markdown("<h1 style='color: darkred; font-size: 3.0em;'>Curriculum Vitae</h1>", unsafe_allow_html=True)

st.markdown(f"# {NAME}")

profile_pic = Image.open(profile_pic_path)

col1, col2 = st.columns(2, gap="small")
with col1:
    # image
    st.image(profile_pic, width=230)
with col2:
    # infos
    st.header('Qui je suis')
    st.write(NAME)
    st.write('Adresse: 68 rue du colonel de rochebrune, 92380 Garches')
    st.write('Email:', EMAIL)
    st.write('Téléphone: +33 6 25 11 77 12')
    st.write(SOCIAL_MEDIA_URL)
    st.download_button(
        label=" 📄 Test CV",
        data=PDFbyte,
        file_name= os.path.basename(fichierpdf),
        mime="application/octet-stream",
    )

# ajout d'espace
st.write("")

# Competences
st.markdown("<h3 style='color: yellow;'>Compétences</h3>", unsafe_allow_html=True)
st.write("Rien pour l'instant dans l'informatique")
st.write("Management d'équipes")
st.write("Planification de projet")

st.write("")

# Expériences professionnelles
st.markdown("<h3 style='color: pink;'>🧭 Mes expériences professionnelles</h3>", unsafe_allow_html=True)

with st.expander("Jardin du Roy (2017-2023)"):
    st.write('Chef de chantier')
    st.write('équipe de 15 personnes')
    st.write("- Management des différentes équipes") 
    st.write("- Plannification des chantiers")
    st.write('- Négociation fournisseurs')
    st.write("- Administratif divers")

with st.expander("Kalozia Garden (2016-2017)"):
    st.write("Chef d'équipe")
    st.write('équipe de 6 personnes')
    st.write("- Management de l'équipe")
    st.write("- Contrôle qualité")
    st.write("- Formation des apprentis")
    st.write("- Administratif divers")


with st.expander("Janet Moyer Landscaping (2011-2016)"):
    st.write('Ouvrier Paysagiste')
    st.write("taille, tonte")
    st.write("contruction de terasse extérieure")
    st.write("maçonnerie diverse")

st.write("")

# Langues
st.markdown("<h3 style='color: pink;'>🌍 Langues</h3>", unsafe_allow_html=True)
display_language_skills()

st.write("")

# formation
st.markdown("<h3 style='color: pink;'> 📜 Formation</h3>", unsafe_allow_html=True)
with st.expander("BAC"):
    st.write("ES spé math")
    st.write('2010, Lycée Richelieu Rueil-Malmaison')
