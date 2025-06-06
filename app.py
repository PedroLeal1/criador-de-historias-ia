import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyBG8DG3bokET1QmKIwWJUQxo3U5KbAUNx0")

model = genai.GenerativeModel("gemini-1.5-flash")  

st.set_page_config(page_title="Criador de Histórias IA")
st.title("Criador de Histórias Interativas com IA")

nome = st.text_input("Nome do Protagonista:")
genero = st.selectbox("Gênero Literário:", ["Fantasia", "Ficção Científica", "Mistério", "Aventura"])
local = st.radio("Local Inicial:", ["Uma floresta antiga", "Uma cidade futurista", "Um castelo assombrado", "Uma nave espacial à deriva"])
frase = st.text_area("Frase de Efeito ou Desafio Inicial:")

if st.button("Gerar Início da História"):
    if nome and frase:
        prompt = f"""Crie o início de uma história de '{genero}' com o protagonista chamado '{nome}'. 
        A história começa em '{local}'. Incorpore a seguinte frase ou desafio no início: '{frase}'.
        Escreva 1 ou 2 parágrafos envolventes."""
        
        try:
            resposta = model.generate_content(prompt)
            st.markdown("###  Início da História:")
            st.write(resposta.text)
        except Exception as e:
            st.error(f"Erro ao gerar a história: {e}")
    else:
        st.warning("Por favor, preencha o nome do protagonista e a frase.")
