class Nodo():
    def __init__(self, nome=None, RG=None, Dat_nasc=None, prox=None, ant=None):
        self.nome = nome
        self.RG = RG
        self.Dat_nasc = Dat_nasc
        self.prox = prox
        self.ant = ant
    
    def __repr__(self):
        ant_str = str(self.ant.nome) if self.ant else "None"
        prox_str = str(self.prox.nome) if self.prox else "None"
        return "%s <- %s -> %s <- %s" % (ant_str, self.nome, prox_str, None)

class ListaDE():
    def __init__(self, cabeca=None):
        self.cabeca = cabeca
        self.cauda = None  # Adicionamos uma referência para a cauda da lista

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

def InsereElemento(lista):
    no = Nodo()
    no.nome = input("Digite o nome: ")
    no.RG = input("Digite o RG: ")
    no.Dat_nasc = input("Digite a data de nascimento: ")
    no.prox = None
    
    if not lista.cabeca:
        lista.cabeca = no
        lista.cauda = no
    else:
        no.ant = lista.cauda
        lista.cauda.prox = no
        lista.cauda = no

def main():
    lista = ListaDE()
    InsereElemento(lista)
    InsereElemento(lista)
    print(lista)

main()
