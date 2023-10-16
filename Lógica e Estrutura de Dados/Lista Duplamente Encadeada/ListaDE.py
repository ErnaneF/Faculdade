class Node:
    def __init__(self, item, anterior, proximo):
        self.item = item
        self.anterior = anterior
        self.proximo = proximo

class Lista:
    cabeca = None
    rabo = None

    def acrescentar(self, item):
        node = Node(item, None, None)

        if self.cabeca is None:
            self.cabeca = node
            self.rabo = node
        else:
            node.anterior = self.rabo
            node.proximo = None

            self.rabo.proximo = node
            self.rabo = node

    def remover(self, item):
        atual = self.cabeca

        while atual:
            if atual.item == item:
                if atual.anterior:
                    atual.anterior.proximo = atual.proximo
                else:
                    self.cabeca = atual.proximo

                if atual.proximo:
                    atual.proximo.anterior = atual.anterior
                return
            atual = atual.proximo

    def imprimirLista(self):
        print("Lista:")

        node = self.cabeca
        no = ""

        while node is not None:
            if node.anterior is None:
                no += "None "
            no += "<---> | " + str(node.item) + " | "
            if node.proximo is None:
                no += "<---> None"

            node = node.proximo
        print(no)
        print("=" * 80)

def main():
    lista = Lista()

    while True:
        opcao = int(input("1-Inserir / 2-Imprimir / 3-Remover / 4-Sair "))

        if opcao == 1:
            lista.acrescentar(input("Digite um item: "))
        elif opcao == 2:
            lista.imprimirLista()
        elif opcao == 3:
            lista.imprimirLista()
            lista.remover(input("Digite o número que deseja remover:  \n"))

        elif opcao == 4:
            break
        else:
            print("Opcao invalida.")

if __name__ == "__main__":
    main()