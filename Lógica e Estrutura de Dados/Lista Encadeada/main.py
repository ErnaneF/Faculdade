class NodoLista:
    def __init__(self, dado = 0, proximo = None):
        self.dado = dado
        self.proximo = proximo

    def __repr__(self): 
        return "%s -> %s" % (self.dado, self.proximo)

class ListaEncadeada():
    def __init__(self, ultimo = None):
        self.ultimo = ultimo

    def __repr__(self):
        return '[' +str(self.ultimo) + ']'
    
#Inserindo novo dado no começo
def InsereComeco(lista, dado):
    novo_nodo = NodoLista(dado)
    novo_nodo.proximo = lista.ultimo
    lista.ultimo = novo_nodo
    

def InsereDepois(lista, nodo_anterior, dado):
    if nodo_anterior is None:
        novo_nodo = NodoLista(dado)
        if lista.ultimo is None:
            lista.ultimo = novo_nodo
        else:
            ultimo_nodo = lista.ultimo
            while ultimo_nodo.proximo is not None:
                ultimo_nodo = ultimo_nodo.proximo
            ultimo_nodo.proximo = novo_nodo
    else:
        novo_nodo = NodoLista(dado)
        novo_nodo.proximo = nodo_anterior.proximo
        nodo_anterior.proximo = novo_nodo





def remove(lista):
        assert lista.ultimo, "Impossível remover valor de lista vazia."
        if lista.ultimo.proximo is None:
            lista.ultimo = None
        else:
            corrente = lista.ultimo
            while corrente.proximo.proximo is not None:
                corrente = corrente.proximo
            corrente.proximo = None



def busca(lista,valor):
    corrente = lista.ultimo

    while corrente and corrente.dado != valor:
        corrente = corrente.proximo
    return corrente

def main():
    lista = ListaEncadeada()
    while True:
        print("\nOpções: ")
        print("1 - Inserir dado no começo.")
        print("2 - Inserir o dado no final da lista.")
        print("3 - Buscar dado dentro da lista.")
        print("4 - Remover último elemento da lista.")
        print("5 - Exibir Lista.")
        print("6 - Para sair.")
        op = int(input("Digite o número da ação desejada: "))

        if op == 1:
            dado = int(input("Digite um número: "))
            InsereComeco(lista, dado)
            nodo_anterior =None

        elif op == 2:
            dado = int(input("Digite um dado para inlcuir no final da lista: "))
            InsereDepois(lista, nodo_anterior, dado)
            
        elif op == 3:
            dado = int(input("Valor a ser buscado: "))
            valor = busca(lista, dado)
            if valor:
                print(f"Elemento {dado} presente na lista. ")
            else:
                print(f"Elemento {dado} não presente na lista.")

        elif op==4:
            remove(lista)
            print("Removido.")

        elif op ==5:
            print(lista)

        elif op == 6:
            print("Saindo...")
            break

        else:
            print("Digite os números dentro do parâmetro.")


main()


