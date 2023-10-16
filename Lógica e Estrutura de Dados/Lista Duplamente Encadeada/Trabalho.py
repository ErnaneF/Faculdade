class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.cabeca = None

    def adicionar_final(self, dado):
        novo_no = No(dado)
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no
            novo_no.anterior = atual

    def exibir(self):
        atual = self.cabeca
        while atual:
            print(atual.dado, end=" <-> ")
            atual = atual.proximo
        print("None")

    def remover(self, dado):
        atual = self.cabeca

        while atual:
            if atual.dado == dado:
                if atual.anterior:
                    atual.anterior.proximo = atual.proximo
                else:
                    self.cabeca = atual.proximo

                if atual.proximo:
                    atual.proximo.anterior = atual.anterior
                return
            atual = atual.proximo


while True:
    lista = ListaDuplamenteEncadeada()
    op =int(input("1 - Inserir um número no final / 2 - Deletar / 3 - Exibir / 4 - Sair "))
    if op == 1:
        lista.adicionar_final(input("Digite um número: "))
    elif op == 2:
        lista.remover(input("Digite o número a ser removido: "))
    elif op == 3:
        lista.exibir()
    else:
        print("saindo...")
        break