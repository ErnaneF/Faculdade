class ConversorMoedas:
    def __init__(self, dolarR = 4.50, euroR = 5.50 ):
        self.dolarR = dolarR
        self.euroR = euroR

    def converterD(self,num):
        print(f"De dólar para real, esse valor é: R${self.dolarR*num}")
    def converterE(self,num):
        print(f"De euro para real, esse valor é: R${self.euroR*num}")
    

convertendo = ConversorMoedas()
while True:
    print("\nOpções:")
    print("Digite 1 para converter seu valor de dólar pra real.")
    print("Digite 2 para converter seu valor de euro para real.")
    print("Digite 3 para sair do programa")
    op = int(input("Escolha uma opção: "))
    
    if op ==1:
        valor = float(input("Digite o valor: US$"))
        convertendo.converterD(valor)
    elif op == 2:
        valor = float(input("Digite o valor: €"))
        convertendo.converterE(valor)
    elif op == 3:
        print("Encerrando o programa.")
        break
    else:
        print("Essa opção não existe, tente novamente.")

        
        