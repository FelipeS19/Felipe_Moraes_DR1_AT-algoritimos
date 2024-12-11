def knapsack_dinamico(pesos, valores, capacidade):
    n = len(pesos)
    
    tabela = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, capacidade + 1):
            if pesos[i - 1] <= j:
                tabela[i][j] = max(tabela[i - 1][j], valores[i - 1] + tabela[i - 1][j - pesos[i - 1]])
            else:
                tabela[i][j] = tabela[i - 1][j]
    
    return tabela[n][capacidade]


pesos = [1, 3, 4, 5]  
valores = [1, 4, 5, 7]  
capacidade = 7  

print("maximo:", knapsack_dinamico(pesos, valores, capacidade))
