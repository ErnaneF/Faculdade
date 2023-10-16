class No:
    def __init__(self, valor, ant=None, prox=None):
        self.valor = valor
        self.ant = ant
        self.prox = prox

    #def __repr__(self):
    #    return "%s <- %s -> %s" % (self.ant.valor, self.valor, self.prox.valor)

class ListaDEC:
    def __init__(self):
        self.tamanho = 0
        self.inicio = None

    def InserirInicio(self, valor):
        novoNo = No(valor)
        #novoNo.valor = valor
        if self.inicio is None:
            novoNo.ant = novoNo
            novoNo.prox = novoNo
            self.inicio = novoNo
        else:
            ultimoNo = self.inicio.ant
            novoNo.ant = ultimoNo
            novoNo.prox = self.inicio
            self.inicio.ant = novoNo
            ultimoNo.prox = novoNo
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
                novoInicio = self.inicio.prox
                novoInicio.ant = noRemovido.ant
                noRemovido.ant.prox = novoInicio
                self.inicio = novoInicio
            self.tamanho -= 1


    def Imprimir(self):
        if self.tamanho == 0:
            print("Lista vazia")
        else:
            noAtual = self.inicio
            while noAtual.prox != self.inicio: 
                print('<-',noAtual.valor, end='->')
                noAtual = noAtual.prox
            print('<-', noAtual.valor, end='->\n')

def main():
    lista = ListaDEC()

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
            print("saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()