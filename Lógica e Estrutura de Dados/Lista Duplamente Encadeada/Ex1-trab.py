#Higor Carneiro 10-15627
#Natallia Soares dos Santos 10-98585
#Joaquim Manoel Carvalho Ontrante 10-98353
#Ernane Manoel da Silva Filho 10-98392

class Node:
    def __init__(self, item,anterior, proximo, quantidade = None, marca = None, ):
        self.item = item
        self.quantidade = quantidade
        self.marca = marca
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

    def remover(self):
        if self.cabeca:
            itemR = self.cabeca.item
            self.cabeca = self.cabeca.proximo
            if self.cabeca:
                self.cabeca.anterior = None
            else:
                self.rabo = None
            print(f"{itemR} foi removido")
        else:
            print("A lista está vazia")
            
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
        opcao = int(input("1-Inserir / 2-Imprimir / 3-Remover Primeiro / 4-Sair / Digite a opção: "))

        if opcao == 1:
            lista.acrescentar(input("Digite um item: "))
        elif opcao == 2:
            lista.imprimirLista()
        elif opcao == 3:
            lista.remover()
        elif opcao == 4:
            break
        else:
            print("Opcao invalida.")

if __name__ == "__main__":
    main()