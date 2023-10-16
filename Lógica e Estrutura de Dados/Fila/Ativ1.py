import datetime as dt

class Arquivo:
    def __init__(self, data = "" , nome= "", nome_solic= "", prox = None):
        self.data = data
        self.nome = nome
        self.nome_solic = nome_solic
        self.prox = prox

class Fila:
    def __init__(self, cabeça = None ):
        self.cabeca = cabeça
        
    def Inserir(self, data, arq, pess):
        arquivo = Arquivo(data, arq, pess)
        if self.cabeca is not None:
            aux = self.cabeca
            while aux.prox:
                aux = aux.prox
            aux.prox = arquivo
        else:
            self.cabeca = arquivo

    def Imprimir(self):
        if self.cabeca is not None:
            aux = self.cabeca
            while aux:
                print("Arquivo:", aux.nome, "/Emissário:", aux.nome_solic,"/(Emitido:", aux.data + ")")
                aux = aux.prox
        else:
            print("Fila de impressão vazia.")


    def Primeiro(self):
        if self.cabeca is not None:
            aux = self.cabeca
            print(f"Arquivo com nome: \"{aux.nome}\", emitido por: {aux.nome_solic}, solicitado em {aux.data} a caminho da impressão.")
            self.cabeca = None
            self.cabeca = aux.prox

        else:
            print("Fila de impressão vazia.")

    def Limpar(self):
        if self.cabeca is not None:
            aux = self.cabeca
            while aux:
                self.cabeca = None
                self.cabeca = aux.prox
                aux = aux.prox
            print("Todos os itens da fila foram cancelado.")
        else:
            print("A fila está vazia.")


def main():
    lista = Fila()

    while True:
        opcao = int(input("1-Inserir / 2-Imprimir / 3- Imprimir primeiro  / 4-Apagar os itens / 5 - Sair / Digite a opção: "))

        if opcao == 1:
            arquivo = input("Digite o arquivo: ")
            pess = input("Insira seu nome: ")
            time = dt.datetime.now()
            data = time.strftime("%d/%m/%Y %X")
            lista.Inserir(data, arquivo, pess)
        elif opcao == 2:
            lista.Imprimir()
        elif opcao == 3:
            lista.Primeiro()
        elif opcao == 4:
            lista.Limpar()
        elif opcao == 4:
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()