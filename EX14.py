class No:
    def __init__(self, chave):
        self.chave = chave  
        self.esquerda = None  
        self.direita = None   

class BST:
    def __init__(self):
        self.raiz = None  

    def inserir(self, chave):
        if self.raiz is None:
            self.raiz = No(chave)  
        else:
            self.inserir_recursivo(self.raiz, chave)

    def inserir_recursivo(self, no, chave):
        if chave < no.chave:
            if no.esquerda is None:
                no.esquerda = No(chave)
            else:
                self.inserir_recursivo(no.esquerda, chave)
        elif chave > no.chave:
            if no.direita is None:
                no.direita = No(chave)
            else:
                self.inserir_recursivo(no.direita, chave)

    def buscar(self, chave):
        return self.recursivo(self.raiz, chave)

    def recursivo(self, no, chave):
        if no is None:
            return False  
        if chave == no.chave:
            return True  
        elif chave < no.chave:
            return self.recursivo(no.esquerda, chave)  
        else:
            return self.recursivo(no.direita, chave)  

bst = BST()

preços = [100, 50, 150, 30, 70, 130, 170]
for preço in preços:
    bst.inserir(preço)

while True:
    preço_buscado = int(input("\nDigite o preço que deseja buscar (ou 0 para sair): "))
    
    if preço_buscado == 0:
        print("Saindo...")
        break
    
    encontrado = bst.buscar(preço_buscado)

    if encontrado:
        print(f"O preço {preço_buscado} esta disponível")
    else:
        print(f"O preço {preço_buscado} não foi encontrado ")
