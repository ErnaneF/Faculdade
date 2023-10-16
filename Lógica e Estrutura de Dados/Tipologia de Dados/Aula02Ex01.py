class Pessoa():
    def __init__(self,nome='', idade='', sexo='', rg='', cpf='', cor='', fone='', cel='', rua='', número='', cidade='', bairro='', cep=''):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.rg = rg
        self.cpf = cpf
        self.cor = cor
        self.fone = fone
        self.cel = cel
        self.rua = rua
        self.número = número
        self.cidade = cidade
        self.bairro = bairro
        self.cep = cep


p1 = Pessoa()
p1.nome = input("Nome: ")
p1.idade =int(input("Idade: ")) 
p1.sexo = input("Sexo: ")
p1.rg = input("RG: ")
p1.cpf = input("CPF: ")
p1.cor = input("Cor: ")
p1.fone = input("Fone: ")
p1.cel = input("Cel: ")
p1.rua = input("Rua: ")
p1.numero = int(input("Número: "))
p1.cidade = input("Cidade: ")
p1.bairro = input("Bairro: ")
p1.cep = input("CEP: ")


print(p1.nome)
print(p1.idade)
print(p1.sexo)
print(p1.rg)
print(p1.cpf)
print(p1.cor)
print(p1.fone)
print(p1.cel)
print(p1.rua)
print(p1.numero)
print(p1.cidade)
print(p1.bairro)
print(p1.cep)
