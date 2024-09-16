import pandas as pd
import streamlit as st

dfp=pd.read_csv('SOCR-HeightWeight.csv')

st.title("DONNES D'ENTRAINEMENT DU MODELE")

st.subheader("DONNEES D'ENTRAINEMENTS SUR LE POIDS, LA TAILLE, L'ÂGE ET LE SEXE.")
st.write(dfp)

st.subheader("DONNEES AYANT PERMIS L'EXTRACTION DE DONNEES POUR LES VARIABLES QUALITATIVES LIES A LA PRATIQUE SPORTIVE")
dft=pd.read_csv("test airline Passenger satisfaction.csv")
st.write(dft)




