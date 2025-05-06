import streamlit as st
from datetime import datetime
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="Radar de Milhas", page_icon="✈️")
st.title("Radar de Milhas")
st.subheader("Busque passagens com milhas em tempo real (via MaxMilhas)")

origem = st.text_input("Origem (ex: GRU)").upper()
destino = st.text_input("Destino (ex: GIG)").upper()
data = st.date_input("Data da viagem", format="DD/MM/YYYY")

if origem and destino and data:
    data_formatada = datetime.strftime(data, "%d-%m-%Y")
    url = f"https://www.maxmilhas.com.br/passagens-aereas/de-{origem}-para-{destino}-em-{data_formatada}"
    
    st.markdown(f"**Consultando:** [MaxMilhas]({url})")

    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Busca um trecho com valor estimado — limitado, pois o site é dinâmico
        resultado = soup.find("span", class_="Text-sc-__sc-1h3w7so-0").text.strip()
        st.success(f"Preço estimado encontrado: {resultado}")
    
    except Exception as e:
        st.error(f"Erro ao buscar: {e}")
