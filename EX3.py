def buscar(nome_procurado, contatos):
    for contato in contatos:
        if contato["nome"].lower() == nome_procurado.lower():
            return f"Contato encontrado: {contato['nome']}, Telefone: {contato['telefone']}"
    return "Contato não encontrado."

contatos = [
    {"nome": "marlon", "telefone": "1234-5678"},
    {"nome": "carla", "telefone": "9876-5432"},
    {"nome": "ana", "telefone": "5555-1234"},
    {"nome": "felipe", "telefone": "4444-5678"},
]

nome_procurado = "Ana"
resultado = buscar(nome_procurado, contatos)
print(resultado)
