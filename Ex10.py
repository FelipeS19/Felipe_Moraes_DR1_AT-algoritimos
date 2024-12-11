class Navegador:
    def __init__(self):
        self.histórico = []
        self.avançar = []
        self.pagina_atual = None

    def visitar(self, página):
        if self.pagina_atual:
            self.histórico.append(self.pagina_atual)
        self.avançar.clear()
        self.pagina_atual = página
        self.exibir_conteudo()

    def voltar(self):
        if self.histórico:
            self.avançar.append(self.pagina_atual)
            self.pagina_atual = self.histórico.pop()
            print(f"\n--- Voltando para: {self.pagina_atual} ---")
            self.exibir_conteudo()
        else:
            print("\nNão há páginas para voltar!")

    def avançar(self):
        if self.avançar:
            self.histórico.append(self.pagina_atual)
            self.pagina_atual = self.avançar.pop()
            print(f"\n--- Avançando para: {self.pagina_atual} ---")
            self.exibir_conteudo()
        else:
            print("\nNão há páginas para avançar!")

    def exibir_conteudo(self):
        if self.pagina_atual == "Página 1":
            print("Conteúdo da Página 1: Marvel é melhor que DC!")
        elif self.pagina_atual == "Página 2":
            print("Conteúdo da Página 2: Game of Thrones !")
        elif self.pagina_atual == "Página 3":
            print("Conteúdo da Página 3: Ciencia da Computação !")

    def obter_atual(self):
        return self.pagina_atual


navegador = Navegador()

navegador.visitar("Página 1")

while True:
    print("\n--- O que você quer fazer? ---")
    print("1 - Voltar")
    print("2 - Avançar")
    print("0 - Sair")
    opção = input("Escolha uma opção (1, 2, 0): ")
    
    if opção == "1":
        navegador.voltar()
    elif opção == "2":
        if navegador.pagina_atual == "Página 1":
            navegador.visitar("Página 2")
        elif navegador.pagina_atual == "Página 2":
            navegador.visitar("Página 3")
        else:
            print("\nVocê já está na última página!")
    elif opção == "0":
        print("\nSaindo...")
        break
    else:
        print("\nOpção inválida. Tente novamente.")
