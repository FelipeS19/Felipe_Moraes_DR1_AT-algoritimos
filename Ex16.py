class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None


class Arvorebinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        if not self.raiz:
            self.raiz = No(chave)
        else:
            self.inserir_recursivo(self.raiz, chave)

    def inserir_recursivo(self, no, chave):
        if chave < no.chave:
            if no.esquerda is None:
                no.esquerda = No(chave)
            else:
                self.inserir_recursivo(no.esquerda, chave)
        else:
            if no.direita is None:
                no.direita = No(chave)
            else:
                self.inserir_recursivo(no.direita, chave)

    def remover(self, chave):
        self.raiz = self.remover_recursivo(self.raiz, chave)

    def remover_recursivo(self, no, chave):
        if no is None:
            return no

        if chave < no.chave:
            no.esquerda = self.remover_recursivo(no.esquerda, chave)
        elif chave > no.chave:
            no.direita = self.remover_recursivo(no.direita, chave)
        else:
            if no.esquerda is None and no.direita is None:
                return None
            elif no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            else:
                min_no = self.min(no.direita)
                no.chave = min_no.chave
                no.direita = self.remover_recursivo(no.direita, min_no.chave)
        return no

    def min(self, no):
        current = no
        while current.esquerda is not None:
            current = current.esquerda
        return current

    def ordem(self):
        self.ordem_recursivo(self.raiz)
        print()  

    def ordem_recursivo(self, no):
        if no:
            self.ordem_recursivo(no.esquerda)
            print(no.chave, end=" ")
            self.ordem_recursivo(no.direita)


arb = Arvorebinaria()
produtos = [45, 25, 65, 20, 30, 60, 70]

for p in produtos:
    arb.inserir(p)

print("Árvore inicial (em ordem):")
arb.ordem()

print("\nRemovendo o produto com código 20 (nó folha):")
arb.remover(20)
arb.ordem()

print("\nRemovendo o produto com código 25 (nó com um filho):")
arb.remover(25)
arb.ordem()

print("\nRemovendo o produto com código 45 (nó com dois filhos):")
arb.remover(45)
arb.ordem()
