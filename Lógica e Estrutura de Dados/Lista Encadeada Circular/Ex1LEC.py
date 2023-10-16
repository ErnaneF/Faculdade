class No:
    def __init__(self, valor, prox=None):
        self.valor = valor
        self.prox = prox

class ListaCircular:
    def __init__(self):
        self.tamanho = 0
        self.inicio = None

    def InserirInicio(self, valor):
        novoNo = No(valor)
        if self.inicio is None:
            novoNo.prox = novoNo
            self.inicio = novoNo
        else:
            novoNo.prox = self.inicio
            noAtual = self.inicio
            while noAtual.prox != self.inicio:
                noAtual = noAtual.prox
            noAtual.prox = novoNo
            self.inicio = novoNo

        self.tamanho += 1

    def Remover(self):
        if self.tamanho == 0:
            print("Sua lista está vazia!")
        else:
            noRemovido = self.inicio
            if self.tamanho == 1:
                self.inicio = None
            else:
                noAtual = self.inicio
                while noAtual.prox != self.inicio:
                    noAtual = noAtual.prox
                noAtual.prox = self.inicio.prox
                self.inicio = self.inicio.prox
            self.tamanho -= 1

    def Imprimir(self):
        if self.tamanho == 0:
            print("Lista vazia")
        else:
            noAtual = self.inicio
            while True:
                print(noAtual.valor, end=' -> ')
                noAtual = noAtual.prox
                if noAtual == self.inicio:
                    break
            print('\n')

def main():
    lista = ListaCircular()

    while True:
        opcao = int(input("1-Inserir / 2-Imprimir / 3-Remover  / 4-Sair / Digite a opção: "))

        if opcao == 1:
            valor = input("Digite um item: ")
            lista.InserirInicio(valor)
        elif opcao == 2:
            lista.Imprimir()
        elif opcao == 3:
            lista.Remover()
        elif opcao == 4:
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
