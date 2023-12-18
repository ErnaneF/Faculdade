#Discentes:
#Ernane
#Victoria
#Antônio
#Brunno

class Cliente:
    def __init__(self, nome, rg, fone):
        self.nome = nome
        self.rg = rg
        self.fone = fone

class Nodo:
    def __init__(self, chave, cliente):
        self.chave = chave
        self.cliente = cliente
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave, cliente):
        self.raiz = self._inserir(self.raiz, chave, cliente)

    def _inserir(self, raiz, chave, cliente):
        if raiz is None:
            return Nodo(chave, cliente)

        if chave < raiz.chave:
            raiz.esquerda = self._inserir(raiz.esquerda, chave, cliente)
        elif chave > raiz.chave:
            raiz.direita = self._inserir(raiz.direita, chave, cliente)

        return raiz

    def procurar_por_nome(self, nome):
        return self._procurar_por_nome(self.raiz, nome)

    def _procurar_por_nome(self, raiz, nome):
        if raiz is None or raiz.cliente.nome == nome:
            return raiz.cliente if raiz else None

        if nome < raiz.cliente.nome:
            return self._procurar_por_nome(raiz.esquerda, nome)
        else:
            return self._procurar_por_nome(raiz.direita, nome)

    def exibir_cadastros(self):
        print("Escolha o tipo de percurso:")
        print("1. Em Ordem")
        print("2. Pós Ordem")
        print("3. Pré-Ordem")

        opcao = int(input("Digite a opção: "))

        if opcao == 1:
            self.em_ordem(self.raiz)
        elif opcao == 2:
            self.pos_ordem(self.raiz)
        elif opcao == 3:
            self.pre_ordem(self.raiz)
        else:
            print("Opção inválida")

    def em_ordem(self, raiz):
        if raiz:
            self.em_ordem(raiz.esquerda)
            print(f"Chave: {raiz.chave}")
            self.em_ordem(raiz.direita)

    def pos_ordem(self, raiz):
        if raiz:
            self.pos_ordem(raiz.esquerda)
            self.pos_ordem(raiz.direita)
            print(f"Chave: {raiz.chave}")

    def pre_ordem(self, raiz):
        if raiz:
            print(f"Chave: {raiz.chave}")
            self.pre_ordem(raiz.esquerda)
            self.pre_ordem(raiz.direita)


def main():
    arvore = ArvoreBinaria()

    while True:
        print("\nMenu:")
        print("1. Inserir cadastro")
        print("2. Procurar por nome")
        print("3. Exibir cadastros")


        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            chave = int(input("Digite a chave para o cadastro: "))
            nome = input("Digite o nome do cliente: ")
            rg = input("Digite o RG do cliente: ")
            fone = input("Digite o telefone do cliente: ")

            cliente = Cliente(nome, rg, fone)
            arvore.inserir(chave, cliente)

        elif opcao == 2:
            nome = input("Digite o nome a ser procurado: ")
            resultado = arvore.procurar_por_nome(nome)

            if resultado:
                print(f"Cadastro encontrado Nome: {resultado.nome}")
            else:
                print("Cadastro não encontrado")

        elif opcao == 3:
            arvore.exibir_cadastros()

        elif opcao == 4:
            print("Saindo do programa. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
