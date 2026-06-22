import streamlit as st
from tradutor import traduzir_texto, detectar_idioma
from leitores import ler_txt, ler_pdf, ler_docx, ler_csv

st.set_page_config(page_title="Tradutor Inteligente", page_icon="🌍")
st.title("🌍 Tradutor Inteligente de Arquivos")
st.markdown("Faça upload, detectamos o idioma e traduzimos para você!")

# Upload do arquivo
arquivo = st.file_uploader("Envie seu arquivo", type=["txt", "pdf", "docx", "csv"])

if arquivo:
    # Lê o conteúdo baseado na extensão
    extensao = arquivo.name.split(".")[-1].lower()
    if extensao == "txt":
        texto = ler_txt(arquivo)
    elif extensao == "pdf":
        texto = ler_pdf(arquivo)
    elif extensao == "docx":
        texto = ler_docx(arquivo)
    elif extensao == "csv":
        texto = ler_csv(arquivo)
    
    # Detecta idioma original
    idioma_origem = detectar_idioma(texto)
    st.info(f"📝 Idioma detectado: **{idioma_origem}**")
    
    # Escolhe o idioma de destino
    idioma_destino = st.selectbox("Traduzir para:", ["inglês", "espanhol", "francês", "alemão", "italiano", "português"])
    
    if st.button("🚀 Traduzir agora"):
        with st.spinner("Traduzindo..."):
            texto_traduzido = traduzir_texto(texto, idioma_destino)
        
        st.subheader("📄 Texto Traduzido")
        st.write(texto_traduzido)
        
        # Botão para baixar o resultado
        st.download_button(
            label="📥 Baixar arquivo traduzido",
            data=texto_traduzido,
            file_name=f"traduzido_{arquivo.name}",
            mime="text/plain"
        )