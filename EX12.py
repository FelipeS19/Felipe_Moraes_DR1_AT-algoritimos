import os

def listar_arquivos(dirr):
    for item in os.listdir(dirr):
        caminho = os.path.join(dirr, item)
        
        if os.path.isfile(caminho):
            print(caminho)  
        elif os.path.isdir(caminho):
            listar_arquivos(caminho)  

diretorio= "D:/faculdade/Prontos e para entregar"  
listar_arquivos(diretorio)
