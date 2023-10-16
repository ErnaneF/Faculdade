class ListaTarefas():
    def __init__(self):
        self.lista = []
    
    def add(self, tarefa):
        self.lista.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada à lista.")

    def remover(self,tarefa):
        if tarefa in self.lista:
            self.lista.pop(0)

    def mostrar(self):
        if self.lista:
            print("Lista de Tarefas: ")
            for index, tarefa in enumerate(self.lista, start=1):
                print(f"{index}. {tarefa}")
        else:
            print("A lista de tarefas está vazia.")


tar = ListaTarefas()
while True:
    print("\nOpções:")
    print("Digite 1 para adicionar!")
    print("Digite 2 para remover a primeira tarefa!")
    print("Digite 3 para mostrar a lista!")
    print("Digite 4 para sair!")
    op = int(input("Escolha uma opção: "))

    if op == 1:
        tarefa = input("Digite a tarefa a ser adicionada: ")
        tar.add(tarefa)
    elif op == 2:
        tar.remover(tarefa)
    elif op == 3:
        tar.mostrar()
    elif op == 4:
        break
    else:
        print("Esse número não pertence às opções")
