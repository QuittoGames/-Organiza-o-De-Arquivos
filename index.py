import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

paths = {
    "Imagens": [".png", ".jpg"],
    "planilhas": [".xlsx", "cvs"],
    "pdfs": [".pdf"],
    "HTML":[".html"],
    "Texto":[".txt",".docx"]
}


path = askdirectory(title="Selecione uma pasta")
listpaths = os.listdir(path)


for arquivo in listpaths:
    nome, extensao = os.path.splitext(arquivo)
    for pasta in paths:
        if extensao in paths[pasta]:
            pasta_path = os.path.join(path, pasta)
            if not os.path.exists(pasta_path):
                os.mkdir(pasta_path)
            arquivo_antigo = os.path.join(path, arquivo)
            arquivo_novo = os.path.join(pasta_path, arquivo)
            os.rename(arquivo_antigo, arquivo_novo)
        else:
            print(f"A Extençao nao pode ser indentidicada: {path}")
