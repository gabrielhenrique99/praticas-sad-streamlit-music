import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

base = pd.read_csv('songs.csv')

st.title('Prática SAD - Music Dataset')
st.header('Base Utilizada')
st.write(base)

# Tirando duplicações pois vi que uma mesma música aparece várias vezes
music_name_drop_duplicates = base.drop_duplicates(subset="Name")

st.subheader('Top 10 músicas mais populares')
top_10_musicas = music_name_drop_duplicates.sort_values(by="Popularity", ascending=False).head(10)
st.table(top_10_musicas[["Name", "Popularity"]])

# Tirando duplicações no nome dos artistas pois os mesmos também aparecem mais de uma vez
artist_name_drop_duplicates = base.drop_duplicates(subset="Artist")

st.subheader('Top 10 artistas mais populares')
top_10_artistas = artist_name_drop_duplicates.sort_values(by="Popularity", ascending=False).head(10)
st.table(top_10_artistas[["Artist", "Popularity"]])

st.subheader('Top 10 artistas com mais músicas')
top_10_artistas = base["Artist"].value_counts().head(10)
fig, ax = plt.subplots()
sbn.barplot(x=top_10_artistas.index, y=top_10_artistas.values, ax=ax)
plt.xticks(rotation=90)
plt.xlabel('Artistas')
plt.ylabel('Número')
st.pyplot(fig)

st.subheader('Escolha um artista do top 10 com mais músicas para ver quais são as músicas')
artista_selecionado = st.selectbox("Selecione um artista", top_10_artistas.index)
filtro = base[base["Artist"] == artista_selecionado].drop(columns=['Lyrics'])
st.table(filtro)

st.subheader('Escolha uma música do top 10 para ver a letra')
musica_selecionada = st.selectbox("Selecione", top_10_musicas)
letra_selecionada = base[base["Name"] == musica_selecionada]["Lyrics"].iloc[0] # Onde descobri o iloc https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html
st.text(letra_selecionada)