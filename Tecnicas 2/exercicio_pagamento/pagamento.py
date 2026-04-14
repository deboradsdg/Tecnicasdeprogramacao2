from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar_pagamento (self, valor):
        pass

class PagamentoPix(Pagamento):
    def processar_pagamento (self, valor):
        return f"Pagamento via Pix no valor de R${valor:.2f}"

class PagamentoCartao(Pagamento):
    def processar_pagamento (self, valor):
        return f"Pagamento via Cartão no valor de R${valor:.2f}"

class PagamentoBoleto(Pagamento):
    def processar_pagamento (self, valor):
        return f"Pagamento via Boleto no valor de R${valor:.2f}"

class PagamentoFactory(ABC):
    
    @abstractmethod
    def criar_pagamento(self):
        pass
    
    def realizar_pagamento(self, valor):
        pagamento = self.criar_pagamento()
        return pagamento.processar_pagamento(valor)
    
class CartaoFactory(PagamentoFactory):
    def criar_pagamento(self):
        return PagamentoCartao()

class PixFactory(PagamentoFactory):
    def criar_pagamento(self):
        return PagamentoPix()

class BoletoFactory(PagamentoFactory):
    def criar_pagamento(self):
        return PagamentoBoleto()
    
def cliente(factory: PagamentoFactory, valor):
    resultado = factory.realizar_pagamento(valor)
    print(resultado)
    
if __name__ == "__main__":
    
    valor_compra = 150.75
    
    #Pagamento Com Cartão
    factory = CartaoFactory()
    cliente(factory, valor_compra)
    
    #Pagamento Com Pix
    factory = PixFactory()
    cliente(factory, valor_compra)
    
    #Pagamento Com Boleto
    factory = BoletoFactory()
    cliente(factory, valor_compra)

    
    


