
nomes = list()
nomes2 = list()

for i in range(4):
    nome = [input(f"Digite o {i+1} nome: ")]
    nomes.append(nome)
print(nomes)

for i in range (2):
    nome = [input(f"Digite o {i+1} nome: ")]
    nomes.insert(i+1, nome)
print(nomes)

for i in range(3):
    nome = [input(f"Digite o {i+1} nome: ")]
    nomes2.append(nome)

nomes.extend(nomes2)
print(nomes)
