def verificar_duplicatas(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return True
        vistos.add(elemento)
    
    return False

lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 4, 5, 3]

print(verificar_duplicatas(lista1))  
print(verificar_duplicatas(lista2))  