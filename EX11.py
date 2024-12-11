class Fila:
    def __init__(self):
        self.fila = []

    def adicionar_chamado(self, chamado):
        self.fila.append(chamado)
        print(f"Chamado '{chamado}' adicionado a fila.")

    def remover_chamado(self):
        if self.fila:
            self.exibir_fila()
            try:
                rem_call = int(input("Digite o numero do chamado que deseja remover: ")) - 1
                if 0 <= rem_call < len(self.fila):
                    chamado = self.fila.pop(rem_call)
                    print(f"Chamado '{chamado}' removido da fila.")
                else:
                    print("Numero de chamado invalido.")
            except ValueError:
                print("Por favor, digite um numero valido.")
        else:
            print("Não tem chamados na fila para remover.")

    def exibir_fila(self):
        if self.fila:
            print("Fila de Chamados:")
            for i, chamado in enumerate(self.fila, 1):
                print(f"{i}. {chamado}")
        else:
            print("A fila está vazia.")

fila_chamados = Fila()

while True:
    print("\nO que você deseja fazer?")
    print("1 - Adicionar chamado")
    print("2 - Remover chamado")
    print("3 - Exibir fila")
    print("0 - Sair")
    opcao = input("Escolha uma opção (1, 2, 3, 0): ")

    if opcao == "1":
        chamado = input("Digite a descrição do chamado: ")
        fila_chamados.adicionar_chamado(chamado)
    elif opcao == "2":
        fila_chamados.remover_chamado()
    elif opcao == "3":
        fila_chamados.exibir_fila()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção invalida.")
