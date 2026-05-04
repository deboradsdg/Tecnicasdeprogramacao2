from abc import ABC, abstractmethod

# Componente
class Item(ABC):
    @abstractmethod
    def mostrar(self, nivel=0):
        pass

# Folha
class Arquivo(Item):
    def __init__(self, nome):
        self.nome = nome

    def mostrar(self, nivel=0):
        # Multiplicamos a string de espaço pelo nível para criar a hierarquia visual
        print("  " * nivel + f"Arquivo: {self.nome}")

# Composto
class Pasta(Item):
    def __init__(self, nome):
        self.nome = nome
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"Pasta: {self.nome}")
        for item in self.itens:
            item.mostrar(nivel + 1)

# USO
root = Pasta("root")
docs = Pasta("documentos")

docs.adicionar(Arquivo("cv.pdf"))
docs.adicionar(Arquivo("relatorio.docx"))

root.adicionar(docs)
root.adicionar(Arquivo("foto.png"))

# Chamada inicial
root.mostrar()







