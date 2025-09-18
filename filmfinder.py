import streamlit as st
import requests

API_KEY = "46d07f61"

st.title("Buscador de películas con OMDb")

title = st.text_input("Introduce el título de una película en inglés:", "Minions")

if st.button("Buscar"):
    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}&plot=full"
    res = requests.get(url)
    data = res.json()

    if data["Response"] == "True":
        st.header(f"{data.get('Title', 'Unknown')} ({data.get('Year', 'N/A')})")

        poster_url = data.get("Poster", "")
        if poster_url and poster_url != "N/A":
            st.image(poster_url, width=250)

        st.subheader("Detalles")
        st.write(f"**Director:** {data.get('Director', 'N/A')}")
        st.write(f"**Actores:** {data.get('Actors', 'N/A')}")
        st.write(f"**Duración:** {data.get('Runtime', 'N/A')}")
        st.write(f"**IMDb Rating:** {data.get('imdbRating', 'N/A')}/10")
        st.write(f"**Metascore:** {data.get('Metascore', 'N/A')}/100")
        st.write(f"**Premios:** {data.get('Awards', 'No info')}")

        st.subheader("Sinopsis")
        st.write(data.get("Plot", "No plot available"))

    else:
        st.error("Película no encontrada")
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: grey;'>by yeray.</p>", unsafe_allow_html=True)
