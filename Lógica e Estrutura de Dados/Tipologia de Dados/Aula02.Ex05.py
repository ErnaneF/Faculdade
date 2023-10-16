class ContaBancaria():
    def __init__(self, num_conta = '', titular = '', saldo = 0):
        self.nc = num_conta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, quantia):
        if quantia >= 0:
            self.saldo += quantia
            print(f"Você depositou {quantia}. Seu novo saldo é de R${self.saldo}")
        else:
            print("Valor de depósito deve ser maior que zero.")
    
    def sacar(self, quantia):
        if self.saldo >= quantia:
            self.saldo = self.saldo - quantia
            print(f"Você sacou {quantia}. Seu novo saldo é de R${self.saldo}")
        else:
            print("Saldo insuficiente para saque.")

    def exibir(self):
        print(f"Seu saldo é de {self.saldo}")


banco = ContaBancaria()
conta = None
while True:
    print("\nOpções:")
    if conta is None:
        print("Digite 1 para criar uma conta")
    else:
        print("Digite 1 para criar uma conta (já existe uma conta)")
    print("Digite 2 para depositar uma quantia nessa conta")
    print("Digite 3 para sacar")
    print("Digite 4 para exibir o saldo da conta")
    print("Digite 5 para sair.")
    op = int(input("Escolha uma opção: "))

    if op == 1:
        if conta is None:
                titular = input("Digite o titular da conta: ")
                nc = input("Digite o número da conta: ")
                conta = ContaBancaria(titular, nc)
                print(f"Parabéns {titular}, agora você faz parte do nosso banco!")
        else:
                print("Uma conta já foi criada.")

    elif op == 2:
        if conta is not None:
            quantia = float(input("Deseja depositar quanto? "))
            banco.depositar(quantia)
        else:
            print("Crie uma conta primeiro.")
    elif op == 3:
        if conta is not None:
            quantia = float(input("Deseja sacar quanto? "))
            banco.sacar(quantia)
        else:
            print("Crie uma conta primeiro.")
    elif op == 4:
        if conta is not None:
            banco.exibir()
        else:
            print("Crie uma conta primeiro.")

    elif op == 5:
        print("Espero que tenhamos ajudado. Até logo!")
        break
    else:
        print("Esse número não pertence às opções")

        

