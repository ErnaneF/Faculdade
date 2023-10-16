class Calculadora():
    def __init__(self):
        pass
    
    def quadrado(self, numeros):
        resultados = [f"O quadrado de {num} é {float(num)**2}" for num in numeros]
        print("\n".join(resultados))

while True:
    escolha = int(input('Quantos números deseja digitar? (Digite 100 para sair): '))
    if escolha == 100:
        print("Adios, muchacho")
        break
    else:
        numeros = [input(f'Digite o {x+1}º número: ') for x in range(escolha)]
        calculador = Calculadora()
        calculador.quadrado(numeros)

