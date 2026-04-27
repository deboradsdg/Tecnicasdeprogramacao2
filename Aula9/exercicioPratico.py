from abc import ABC, abstractmethod

# 1. Componente Base (Interface)
#Classe abstrata com os metodos que usaremos: Descrição e custo, descrição é string e custo é float
class Pizza(ABC):
    @abstractmethod
    def get_descricao(self) -> str:
        pass
    
    @abstractmethod
    def get_custo(self) -> float:
        pass

# 2. Componente Concreto (A pizza base)
# Ponto de partida, a pizza base com custo definido de 20,00
class PizzaBase(Pizza):
    def get_descricao(self) -> str:
        return "Pizza de Massa Tradicional"
    
    def get_custo(self) -> float:
        return 20.00

# 3. Decorator Base
#Criamos uma classe, com uma "pizza ja decorada", sera nela que vamos incluir os ingredientes e somar os custos
class PizzaDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza

    def get_descricao(self) -> str:
        return self._pizza.get_descricao()

    def get_custo(self) -> float:
        return self._pizza.get_custo()

# 4. Decoradores Concretos (Ingredientes)
#Vamos descrver cada ingrediente a mais como classe, coloar na pizzadecorator (a pizza que ja estava coma base), no valor consideramos o valor já existente, + o valor do ingrediente, garantindo a soma
class Queijo(PizzaDecorator):
    def get_descricao(self) -> str:
        return f"{self._pizza.get_descricao()}, Queijo"
    
    def get_custo(self) -> float:
        return self._pizza.get_custo() + 5.00

class Calabresa(PizzaDecorator):
    def get_descricao(self) -> str:
        return f"{self._pizza.get_descricao()}, Calabresa"
    
    def get_custo(self) -> float:
        return self._pizza.get_custo() + 7.00

class Bacon(PizzaDecorator):
    def get_descricao(self) -> str:
        return f"{self._pizza.get_descricao()}, Bacon"
    
    def get_custo(self) -> float:
        return self._pizza.get_custo() + 8.00

class BordaRecheada(PizzaDecorator):
    def get_descricao(self) -> str:
        return f"{self._pizza.get_descricao()}, Borda Recheada"
    
    def get_custo(self) -> float:
        return self._pizza.get_custo() + 6.00

# --- Teste do Sistema ---

if __name__ == "__main__":
    # Começamos com a pizza simples
    #criamos a minha pizza, e acrescentamos a pizza base
    minha_pizza = PizzaBase()
    
    # Adicionamos ingredientes (decorando o objeto)
    minha_pizza = Queijo(minha_pizza)
    minha_pizza = Calabresa(minha_pizza)
    minha_pizza = BordaRecheada(minha_pizza)

  #Impressaõ do pedido final 
    print("--- Seu Pedido ---")
    print(f"Descrição: {minha_pizza.get_descricao()}")
    print(f"Total: R$ {minha_pizza.get_custo():.2f}")
