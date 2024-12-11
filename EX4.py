import random
import time

def binario(lista, isbn_procurado):
    A, B = 0, len(lista) - 1
    cont = 0
    while A <= B:
        cont += 1
        meio = (A + B) // 2
        if lista[meio] == isbn_procurado:
            return meio, cont
        elif lista[meio] < isbn_procurado:
            A = meio + 1
        else:
            B = meio - 1
    return -1, cont

def linear(lista, isbn_procurado):
    cont = 0
    for i in range(len(lista)):
        cont += 1
        if lista[i] == isbn_procurado:
            return i, cont
    return -1, cont

random.seed(42)
isbn_lista = sorted(random.sample(range(1_000_000, 10_000_000), 100_000))

isbn_procurado = random.choice(isbn_lista)


inicio_binaria = time.time()
resultado_binaria, cont_binaria = binario(isbn_lista, isbn_procurado)
fim_binaria = time.time()


inicio_linear = time.time()
resultado_linear, cont_linear = linear(isbn_lista, isbn_procurado)
fim_linear = time.time()

print(f"""=== Resultados da Busca ===
ISBN procurado: {isbn_procurado}

Busca Binária:
Posição: {resultado_binaria}
Iterações: {cont_binaria}
Tempo: {fim_binaria - inicio_binaria:.6f} segundos
""")

print(f"""\nBusca Linear:
Posição: {resultado_linear}
Iterações: {cont_linear}
Tempo: {fim_linear - inicio_linear:.6f} segundos
""")

