
class Aluno():
    def __init__(self, nome='',ra='',matemática=[], português=[]):
        self.nome = nome
        self.ra = ra
        self.matemática = matemática
        self.português = português

a1 = Aluno()
a1.nome = input("Nome: ")
a1.ra = input("RA: ")

print("Digite suas notas de matemática")
for x in range(4):
    a1.matemática.append(float(input(f"Digite a {x+1}º nota ")))
    mm = sum(a1.matemática)/len(a1.matemática)

print("Digite suas notas de português")
for x in range(4):
    a1.português.append(float(input(f"Digite a {x+1}º nota ")))
    mp = sum(a1.português)/len(a1.português)

print("Nome: ", a1.nome)
print("RA: ", a1.ra)
print("Média das notas de matemática: ", mm)
print("Média das notas de português: ", mp)
