import copy

class Personagem:
    def __init__(self, nome, vida, arma, habilidades):
        self.nome = nome
        self.vida = vida
        self.arma = arma
        self.habilidades = habilidades

    def clone(self):
        return copy.deepcopy(self)
    
    def mostrar(self):
        print("Nome: ", self.nome)
        print("Vida: ", self.vida)
        print("Arma: ", self.arma)
        print("Habilidades: ", self.habilidades)

# Criando um protótipo (Corrigido o '-')
guerreiro_prototipo = Personagem("Guerreiro", 100, "Espada", ["Ataque forte", "Defesa"])

# Clonando o protótipo (Corrigido o espaço vazio)
guerreiro1 = guerreiro_prototipo.clone()
guerreiro2 = guerreiro_prototipo.clone()

# Modificando os clones
guerreiro1.nome = "Guerreiro A"
guerreiro2.nome = "Guerreiro B"

# Exibindo
guerreiro1.mostrar()
print()
guerreiro2.mostrar()



