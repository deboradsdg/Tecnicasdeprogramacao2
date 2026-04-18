
from abc import ABC, abstractmethod

class Botao (ABC):
    @abstractmethod
    def renderizar(self):
        pass

class Checkbok(ABC):
    @abstractmethod
    def marcar(self):
        pass

class BotaoWindows(Botao):
    def renderizar(self):
        return "Renderizando botão no estilo Windows"


class BotaoLinux(Botao):
    def renderizar(self):
        return "Renderizando botão no estilo Linux"

class CheckbokWindows(Checkbok):
    def marcar(self):
        return "Checkbox Windows marcado"

class CheckbokLinux(Checkbok):
    def marcar(self):
        return "Checkbox Linux marcado"

class FabricaGUI(ABC):

    @abstractmethod
    def criar_botao(self):
        pass

    @abstractmethod
    def criar_checkbox(self):
        pass

class FabricaWindows(FabricaGUI):
    def criar_botao(self):
        return BotaoWindows()

    def criar_checkbox(self):
        return CheckbokWindows()

class FabricaLinux(FabricaGUI):
    def criar_botao(self):
        return BotaoLinux()

    def criar_checkbox(self):
        return CheckbokLinux()


def cliente(fabrica: FabricaGUI):
    botao = fabrica.criar_botao()
    checkbox = fabrica.criar_checkbox()

    print(botao.renderizar())
    print(checkbox.marcar())

if __name__ == "__main__":
    fabrica = FabricaWindows()
    cliente(fabrica)

    fabrica = FabricaLinux()
    cliente(fabrica)