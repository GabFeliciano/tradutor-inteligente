import PyPDF2
import docx
import pandas as pd
import io

def ler_txt(arquivo):
    return arquivo.read().decode("utf-8")

def ler_pdf(arquivo):
    leitor = PyPDF2.PdfReader(arquivo)
    texto = ""
    for pagina in leitor.pages:
        texto += pagina.extract_text()
    return texto

def ler_docx(arquivo):
    doc = docx.Document(io.BytesIO(arquivo.read()))
    texto = "\n".join([paragrafo.text for paragrafo in doc.paragraphs])
    return texto

def ler_csv(arquivo):
    df = pd.read_csv(arquivo)
    return df.to_string()