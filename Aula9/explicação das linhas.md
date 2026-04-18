Linhas 06 a 07 (@abstractmethod): Elas criam um "contrato". Ao marcar esses métodos como abstratos dentro de uma classe que herda de ABC, você garante que qualquer nova bebida (como CafeSimples) ou qualquer decorador seja obrigado a escrever sua própria versão desses métodos. Se você esquecer de um deles, o Python não deixará você instanciar a classe.

Linhas 17 a 26 (DecoradorBebida): Esta é a "casca" do decorador.

O __init__ permite que você passe uma bebida para dentro de outra (ex: colocar um café dentro de um copo com leite).

Os métodos custo e descricao nessas linhas são chamados de repasses. Eles garantem que, se o decorador não fizer nada de especial, ele apenas passará a pergunta adiante para o objeto que ele está guardando. Isso permite que você empilhe quantos decoradores quiser!