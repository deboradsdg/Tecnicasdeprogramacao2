from abc import ABC, abstractmethod

class Notificacao(ABC):
    @abstractmethod
    def enviar (self, mensagem):
        pass

class EmailNotificacao(Notificacao):
    def enviar (self, mensagem):
        return f"Enviando email: {mensagem}"

class SMSNotificacao(Notificacao):
    def enviar (self, mensagem):
        return f"Enviando SMS: {mensagem}"

class PushNotificacao(Notificacao):
     def enviar (self, mensagem):
        return f"Enviando Push: {mensagem}"


class NotificacaoFactory(ABC):

    @abstractmethod
    def criar_notificacao(self):
        pass
    
    def notificar(self, mensagem):
        notificacao = self.criar_notificacao()
        return notificacao.enviar(mensagem)
    
class EmailFactory(NotificacaoFactory):
    def criar_notificacao(self):
        return EmailNotificacao()

class SMSFactory(NotificacaoFactory):
    def criar_notificacao(self):
        return SMSNotificacao()

class PushFactory(NotificacaoFactory):
    def criar_notificacao(self):
        return PushNotificacao()


def cliente (factory: NotificacaoFactory):
    print(factory.notificar("Olá usuário!"))

if __name__ == "__main__":
    factory = EmailFactory()
    cliente(factory)

    factory = SMSFactory()
    cliente(factory)

    factory = PushFactory()
    cliente(factory)