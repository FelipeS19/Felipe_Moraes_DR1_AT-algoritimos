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

    def buscar_min(self):
        return self.buscar_min_recursivo(self.raiz)

    def buscar_min_recursivo(self, no):
        if no.esquerda is None:
            return no.chave
        else:
            return self.buscar_min_recursivo(no.esquerda)

    def buscar_max(self):
        return self.buscar_max_recursivo(self.raiz)

    def buscar_max_recursivo(self, no):
        if no.direita is None:
            return no.chave
        else:
            return self.buscar_max_recursivo(no.direita)

bst = BST()

notas = [85, 70, 95, 60, 75, 90, 100]
for nota in notas:
    bst.inserir(nota)

nota_minima = bst.buscar_min()
nota_maxima = bst.buscar_max()

print(f"A nota minima é: {nota_minima}")
print(f"A nota maxima é: {nota_maxima}")
