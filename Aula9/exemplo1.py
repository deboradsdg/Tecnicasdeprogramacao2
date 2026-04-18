from abc import ABC, abstractmethod

# Componente 
class Bebida(ABC):
    @abstractmethod
    def custo(self):
        # Define que toda bebida DEVE implementar o cálculo de custo
        pass

    @abstractmethod
    def descricao(self):
        # Define que toda bebida DEVE implementar uma descrição textual
        pass

# Componente Concreto
class CafeSimples(Bebida):
    def custo(self):
        return 5.0

    def descricao(self):
        return "Café Simples"

# Decorator - Corrigido o nome e implementado os métodos base
class DecoradorBebida(Bebida):
    def __init__(self, bebida):
        # Recebe um objeto do tipo Bebida e o armazena para ser "decorado"
        self._bebida = bebida
    
    def custo(self):
        # Delega a chamada do custo para o objeto que está dentro do decorador
        return self._bebida.custo()

    def descricao(self):
        # Delega a chamada da descrição para o objeto que está dentro do decorador
        return self._bebida.descricao()

# Decoradores Concretos
class Leite(DecoradorBebida):
    def custo(self):
        return super().custo() + 2.0

    def descricao(self):
        return super().descricao() + ", Leite"

class Chocolate(DecoradorBebida):
    def custo(self):
        return super().custo() + 3.0

    def descricao(self):
        return super().descricao() + ", Chocolate"

# Utilização 
minha_bebida = CafeSimples()
minha_bebida = Leite(minha_bebida)
minha_bebida = Chocolate(minha_bebida)

print("Descrição:", minha_bebida.descricao())
print(f"Custo: R$ {minha_bebida.custo():.2f}")