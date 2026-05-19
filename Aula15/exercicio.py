from abc import ABC, abstractmethod


# =====================================================
# FACTORY METHOD
# =====================================================

# Classe abstrata de pagamento
class Pagamento(ABC):

    @abstractmethod
    def pagar(self, valor):
        pass


# Pagamento com cartão
class PagamentoCartao(Pagamento):

    def pagar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} realizado com CARTÃO.")


# Pagamento com PIX
class PagamentoPix(Pagamento):

    def pagar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} realizado com PIX.")


# Pagamento com Boleto
class PagamentoBoleto(Pagamento):

    def pagar(self, valor):
        print(f"Boleto gerado no valor de R$ {valor:.2f}. Aguardando pagamento.")


# Factory Method atualizado
class FabricaPagamento:

    @staticmethod
    def criar_pagamento(tipo):
        tipo = tipo.lower()  # Evita problemas com maiúsculas/minúsculas
        
        if tipo == "cartao":
            return PagamentoCartao()
        elif tipo == "pix":
            return PagamentoPix()
        elif tipo == "boleto": # boleto
            return PagamentoBoleto()
        else:
            raise ValueError(f"Tipo de pagamento '{tipo}' inválido.")


# =====================================================
# CHAIN OF RESPONSIBILITY
# =====================================================

# Classe base dos validadores
class Validador:

    def __init__(self):
        self.proximo = None

    def definir_proximo(self, proximo):
        self.proximo = proximo
        return proximo

    def processar(self, pedido):
        if self.proximo:
            return self.proximo.processar(pedido)
        return True


# Verifica estoque
class ValidarEstoque(Validador):

    def processar(self, pedido):
        if pedido["estoque"] <= 0:
            print("Produto sem estoque.")
            return False

        print("Estoque validado.")
        return super().processar(pedido)


# Verifica valor mínimo
class ValidarValorMinimo(Validador):

    def processar(self, pedido):
        if pedido["valor"] < 10:
            print("Pedido abaixo do valor mínimo.")
            return False

        print("Valor mínimo validado.")
        return super().processar(pedido)


# Verifica CPF (Com cálculo real dos dígitos verificadores)
class ValidarCPF(Validador):

    def _cpf_valido(self, cpf: str) -> bool:
        # Remove caracteres não numéricos (caso venha com pontos ou hífen)
        cpf = "".join(filter(str.isdigit, cpf))

        # Verifica se tem 11 dígitos ou se são todos números repetidos (ex: 111.111.111-11)
        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False

        # Cálculo do primeiro dígito verificador
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        resto = (soma * 10) % 11
        digito_1 = 0 if resto == 10 else resto

        # Cálculo do segundo dígito verificador
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        resto = (soma * 10) % 11
        digito_2 = 0 if resto == 10 else resto

        # Compara os dígitos calculados com os originais
        return int(cpf[9]) == digito_1 and int(cpf[10]) == digito_2

    def processar(self, pedido):
        if not self._cpf_valido(pedido["cpf"]):
            print(f"CPF '{pedido['cpf']}' inválido.")
            return False

        print("CPF validado com sucesso.")
        return super().processar(pedido)


# =====================================================
# FACADE
# =====================================================

class SistemaPedido:

    def finalizar_pedido(self, pedido, tipo_pagamento):
        print("Iniciando pedido...\n")

        # Criando a cadeia de validação
        estoque = ValidarEstoque()
        valor = ValidarValorMinimo()
        cpf = ValidarCPF()

        estoque.definir_proximo(valor).definir_proximo(cpf)

        # Executando validações
        if estoque.processar(pedido):
            print("\nPedido aprovado.")
            try:
                pagamento = FabricaPagamento.criar_pagamento(tipo_pagamento)
                pagamento.pagar(pedido["valor"])
                print("Pedido finalizado com sucesso.")
            except ValueError as e:
                print(f"Erro no pagamento: {e}")
                print("Pedido cancelado por falha no método de pagamento.")
        else:
            print("\nPedido cancelado.")



# CPF válido gerado para testes (pode testar com outros válidos)
pedido_sucesso = {
    "valor": 150,
    "estoque": 10,
    "cpf": "41434973055"  
}

sistema = SistemaPedido()

print("--- TESTE 1: Boleto com CPF Válido ---")
sistema.finalizar_pedido(pedido_sucesso, "boleto")

print("\n" + "="*40 + "\n")


pedido_falha_cpf = {
    "valor": 150,
    "estoque": 10,
    "cpf": "12345678901"  # CPF inválido na regra de dígitos
}

print("--- TESTE 2: PIX com CPF Inválido ---")
sistema.finalizar_pedido(pedido_falha_cpf, "pix")
