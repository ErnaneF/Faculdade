escolha = int(input('Digite quantas pessoas quer escrever: '))

pessoas = [(input("Digite um nome: "), int(input("Digite a idade: "))) for _ in range(escolha)]

print(pessoas)