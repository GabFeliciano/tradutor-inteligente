from deep_translator import GoogleTranslator
from langdetect import detect

def detectar_idioma(texto):
    try:
        return detect(texto)
    except:
        return "idioma não identificado"

def traduzir_texto(texto, idioma_destino):
    # Mapeia o nome do idioma para o código usado pela API
    mapa = {
        "inglês": "en",
        "espanhol": "es",
        "francês": "fr",
        "alemão": "de",
        "italiano": "it",
        "português": "pt"
    }
    destino = mapa.get(idioma_destino, "en")
    
    # Traduz
    tradutor = GoogleTranslator(target=destino)
    return tradutor.translate(texto)