class Computador:
    def __init__(self):
        self.cpu = None
        self.memoria = None
        self.armazenamento = None
        self.gpu = None

    def especificacoes(self):
        print(f"CPU: {self.cpu}")
        print(f"Memória: {self.memoria}")
        print(f"Armazenamento: {self.armazenamento}")
        print(f"GPU: {self.gpu}")

class ComputadorBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self.computador = Computador()

    def adicionar_cpu(self, cpu):
        self.computador.cpu = cpu
    
    def adicionar_memoria(self, memoria):
        self.computador.memoria = memoria

    def adicionar_armazenamento(self, armazenamento):
        self.computador.armazenamento = armazenamento

    # CORREÇÃO 1: Adicionado o método que faltava
    def adicionar_gpu(self, gpu):
        self.computador.gpu = gpu

    # CORREÇÃO 2: Adicionado o método para retornar o objeto pronto
    def obter_resultado(self):
        produto = self.computador
        self.reset() # Limpa o builder para a próxima construção
        return produto
         
class Diretor:
    def __init__(self, builder):
        self.builder = builder

    def construir_pc_gamer(self):
        self.builder.adicionar_cpu("Intel i9")
        self.builder.adicionar_memoria("32GB")
        self.builder.adicionar_armazenamento("1TB SSD")
        self.builder.adicionar_gpu("RTX 4080")

    def construir_pc_escritorio(self):
        self.builder.adicionar_cpu("Intel i5")
        self.builder.adicionar_memoria("16GB")
        self.builder.adicionar_armazenamento("512GB SSD")
        self.builder.adicionar_gpu("Integrada")

# Execução
builder = ComputadorBuilder()
diretor = Diretor(builder)

diretor.construir_pc_gamer()
pc = builder.obter_resultado()
pc.especificacoes()
