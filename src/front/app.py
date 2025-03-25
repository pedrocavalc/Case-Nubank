import streamlit as st
import pandas as pd
import requests
import ast

API_URL = "http://localhost:8000/recommend"
PLATFORM_LINKS = {
    "amazon": "https://www.primevideo.com",
    "apple": "https://tv.apple.com",
    "hbo": "https://www.hbomax.com",
    "netflix": "https://www.netflix.com",
}
def get_movie_poster(imdb_id):
    OMDB_API_KEY = "a89eb03f"
    url = f"http://www.omdbapi.com/?i={imdb_id}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("Poster")
    return None

st.set_page_config(page_title="Movie Recommender", layout="centered")
@st.cache_data
def load_data():
    df = pd.read_csv("../../data/processed/plataform_data.csv")
    return df

plataform_df = load_data()

st.title("🎬 Movie Recommender")

st.write("Insira os IDs dos seus filmes favoritos (imdbId), separados por vírgula:")

favorite_ids_input = st.text_area("IDs dos filmes", placeholder="tt0111161,tt0068646,tt0071562")

if st.button("Obter Recomendações"):
    favorite_ids = [id.strip() for id in favorite_ids_input.split(",") if id.strip()]

    if not favorite_ids:
        st.warning("Por favor, insira ao menos um ID de filme.")
    else:
        with st.spinner("Consultando modelo..."):
            try:
                response = requests.post(API_URL, json={"favorite_ids": favorite_ids})
                response.raise_for_status()
                data = response.json()
                recommended_ids = data.get("recommended_ids", [])

                if recommended_ids:
                    st.success("✅ Recomendações geradas com sucesso!")

                    recommended_movies = plataform_df[plataform_df["imdbId"].isin(recommended_ids)]
                    if not recommended_movies.empty:
                        st.subheader("🎥 Filmes recomendados:")
                        for _, row in recommended_movies.iterrows():
                            col1, col2 = st.columns([1, 3])
                            with col1:
                                poster_url = get_movie_poster(row["imdbId"])
                                if poster_url and poster_url != "N/A":
                                    st.image(poster_url, use_column_width=True)
                                else:
                                    st.write("❌ Sem imagem")
                            with col2:
                                st.markdown(f"**{row['title']}**")
                                st.write(f"IMDb ID: {row['imdbId']}")

                                platforms = row.get("platform", "[]")
                                try:
                                    platforms_list = ast.literal_eval(platforms) if isinstance(platforms, str) else platforms
                                    if platforms_list:
                                        links = [
                                            f"[{p.capitalize()}]({PLATFORM_LINKS.get(p, '#')})"
                                            for p in platforms_list
                                        ]
                                        platforms_str = " | ".join(links)
                                    else:
                                        platforms_str = "Não disponível"
                                except:
                                    platforms_str = "Não disponível"

                                st.write(f"📺 Plataformas: {platforms_str}")
                    else:
                        st.warning("IDs recomendados não foram encontrados no dataset.")
                else:
                    st.info("Nenhuma recomendação foi retornada.")

            except requests.exceptions.RequestException as e:
                st.error(f"Erro ao conectar com a API: {e}")
