from abc import ABC, abstractmethod

# Componente Base
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass

# Componente Concreto 
class NotificadorEmail(Notificador):
    def enviar(self, mensagem):
        return f"Enviando por Email: {mensagem}"

# Decorator Base
class DecoradorNotificador(Notificador):
    def __init__(self, notificador: Notificador):
        self._notificador = notificador

    def enviar(self, mensagem):
        return self._notificador.enviar(mensagem)

# Decoradores Concretos
class NotificadorSMS(DecoradorNotificador):
    def enviar(self, mensagem):
        # Chama o componente anterior e adiciona sua própria funcionalidade
        return self._notificador.enviar(mensagem) + \
               f"\nEnviando por SMS: {mensagem}"

class NotificadorWhatsapp(DecoradorNotificador):
    def enviar(self, mensagem):
        return self._notificador.enviar(mensagem) + \
               f"\nEnviando por WhatsApp: {mensagem}"

# Utilização
# Começamos com o objeto base
notificador = NotificadorEmail()

# "Envolvemos" o objeto com camadas adicionais (Decorators)
notificador = NotificadorSMS(notificador)
notificador = NotificadorWhatsapp(notificador)

# Execução
print(notificador.enviar("Alerta de Sistema!"))