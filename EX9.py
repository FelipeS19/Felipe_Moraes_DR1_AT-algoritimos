class RedeSocial:
    def __init__(self):
        self.perfis = {}
    
    def add_perfil(self, nome_usuario, perfil):
        self.perfis[nome_usuario] = perfil
    
    def recuperar(self, nome_usuario):
        return self.perfis.get(nome_usuario, "Usuário não encontrado")


sistema = RedeSocial()

sistema.add_perfil("usuario1", {"nome": "Nathan", "idade": 25, "cidade": "São Paulo"})
sistema.add_perfil("usuario2", {"nome": "Amanda", "idade": 30, "cidade": "Rio de Janeiro"})
sistema.add_perfil("usuario3", {"nome": "Carlos", "idade": 22, "cidade": "Belo Horizonte"})

perfil_usuario1 = sistema.recuperar("usuario1")
perfil_usuario2 = sistema.recuperar("usuario2")
perfil_inexistente = sistema.recuperar("usuario4")

print(perfil_usuario1)  
print(perfil_usuario2)  
print(perfil_inexistente)  
