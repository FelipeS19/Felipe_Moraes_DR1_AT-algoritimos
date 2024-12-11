def sort_jogadores(jogadores):
    n = len(jogadores)
    for i in range(n):
        indice_maior = i
        for j in range(i + 1, n):
            if jogadores[j]["pontuacao"] > jogadores[indice_maior]["pontuacao"]:
                indice_maior = j
        jogadores[i], jogadores[indice_maior] = jogadores[indice_maior], jogadores[i]

jogadores = [
    {"nome": "Carlos", "pontuacao": 1200},
    {"nome": "pedro", "pontuacao": 800},
    {"nome": "felipe", "pontuacao": 1500},
    {"nome": "matheus", "pontuacao": 1000},
]

sort_jogadores(jogadores)

for jogador in jogadores:
    print(f"{jogador['nome']} - Pontuação: {jogador['pontuacao']}")
