import random
import time

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def tempo(tamanho):
    lista_precos = [random.uniform(1, 1000) for _ in range(tamanho)]
    inicio = time.time()
    bubble_sort(lista_precos)
    fim = time.time()
    return fim - inicio

# Teste com 1 mil elementos
tempo_1000 = tempo(1000)
print(f"Tempo para 1.000 elementos: {tempo_1000:.6f} segundos")

# Teste com 10 mil elementos
tempo_10000 = tempo(10000)
print(f"Tempo para 10.000 elementos: {tempo_10000:.6f} segundos")
