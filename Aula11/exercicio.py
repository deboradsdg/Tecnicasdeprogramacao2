from abc import ABC, abstractmethod

# 1. Classe base
class ItemMenu(ABC):
    @abstractmethod
    def get_preco(self):
        pass


class Prato(ItemMenu):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def get_preco(self):
        return self.preco


class Combo(ItemMenu):
    def __init__(self, nome):
        self.nome = nome
        self.itens = []

    def adicionar(self, item: ItemMenu):
        self.itens.append(item)

    def get_preco(self):
        # O preço do combo é a soma de todos os seus itens
        total = sum(item.get_preco() for item in self.itens)
        return total

-


hamburguer = Prato("Hambúrguer", 25.00)
batata = Prato("Batata Frita", 12.00)
refrigerante = Prato("Refrigerante", 8.00)
sobremesa = Prato("Sorvete", 10.00)


combo_executivo = Combo("Combo Executivo")
combo_executivo.adicionar(hamburguer)
combo_executivo.adicionar(batata)


combo_familia = Combo("Combo Família")
combo_familia.adicionar(combo_executivo) # Adicionando o combo anterior
combo_familia.adicionar(refrigerante)
combo_familia.adicionar(sobremesa)


print(f"Preço {hamburguer.nome}: R$ {hamburguer.get_preco():.2f}")
print(f"Preço {combo_executivo.nome}: R$ {combo_executivo.get_preco():.2f}")
print(f"Preço {combo_familia.nome} (Total com itens aninhados): R$ {combo_familia.get_preco():.2f}")
