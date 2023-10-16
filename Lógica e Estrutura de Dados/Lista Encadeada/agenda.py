class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __repr__(self):
        return f" Nome: {self.nome} - Telefone: {self.telefone}, Email: {self.email}"

class NodoLista:
    def __init__(self, dado=None, proximo=None):
        self.dado = dado
        self.proximo = proximo

    def __repr__(self):
        return f"{self.dado}"

class ListaEncadeada:
    def __init__(self):
        self.ultimo = None

    def __repr__(self):
        if self.ultimo is None:
            return '[]'
        result = '['
        current = self.ultimo
        while current is not None:
            result += str(current.dado)
            if current.proximo is not None:
                result += ', '
            current = current.proximo
        result += ']'
        return result

    def remove_ultimo_contato(self):
        assert self.ultimo, "Impossível remover contato de uma lista vazia."
        if self.ultimo.proximo is None:
            self.ultimo = None
        else:
            anterior = None
            atual = self.ultimo
            while atual.proximo is not None:
                anterior = atual
                atual = atual.proximo
            anterior.proximo = None

# Inserindo novo dado no começo
def InsereComeco(lista, contato):
    novo_nodo = NodoLista(contato)
    novo_nodo.proximo = lista.ultimo
    lista.ultimo = novo_nodo

def InsereOrdenado(lista, contato):
    novo_nodo = NodoLista(contato)
    if lista.ultimo is None:
        lista.ultimo = novo_nodo
    else:
        anterior = None
        atual = lista.ultimo
        while atual is not None and atual.dado.nome < contato.nome:
            anterior = atual
            atual = atual.proximo
        if anterior is None:
            novo_nodo.proximo = lista.ultimo
            lista.ultimo = novo_nodo
        else:
            novo_nodo.proximo = atual
            anterior.proximo = novo_nodo

def main():
    lista = ListaEncadeada()
    while True:
        print("\nOpções:")
        print("1 - Inserir contato no começo.")
        print("2 - Inserir contato em ordem alfabética.")
        print("3 - Buscar contato por nome.")
        print("4 - Remover último contato da lista.")
        print("5 - Exibir Lista de Contatos.")
        print("6 - Para sair.")
        op = int(input("Digite o número da ação desejada: "))

        if op == 1:
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            email = input("Digite o email do contato: ")
            contato = Contato(nome, telefone, email)
            InsereComeco(lista, contato)

        elif op == 2:
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            email = input("Digite o email do contato: ")
            contato = Contato(nome, telefone, email)
            InsereOrdenado(lista, contato)

        elif op == 3:
            nome = input("Nome a ser buscado: ")
            encontrado = False
            current = lista.ultimo
            while current is not None:
                if current.dado.nome == nome:
                    print(f"Contato encontrado: {current.dado}")
                    encontrado = True
                    break
                current = current.proximo
            if not encontrado:
                print(f"Contato com o nome {nome} não encontrado.")

        elif op == 4:
            lista.remove_ultimo_contato()
            print("Último contato removido.")

        elif op == 5:
            print("Lista de Contatos:")
            print(lista)

        elif op == 6:
            print("Saindo...")
            break

        else:
            print("Digite um número dentro do parâmetro.")

if __name__ == "__main__":
    main()
