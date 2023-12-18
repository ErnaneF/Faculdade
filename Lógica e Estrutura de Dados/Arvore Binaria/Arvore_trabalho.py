class Nodo:
    def __init__(self, dado, nome, rg, fone):
        self.dado = dado
        self.nome = nome
        self.rg = rg
        self.fone = fone
        self.direita = None
        self.esquerda = None

class ArvoreB:
    def __init__(self, raiz = None):
        self.raiz = raiz
    
    def inserir(self,dado):
        self.raiz = self._inserir_recursivamente(self.raiz, dado)
    
    def _inserir_recursivamente(self,raiz,dado):
        if raiz is None:
            return Nodo(dado)
        if dado == raiz.dado:
            print("Número duplicado. Não será inserido.")
            return raiz
        
        elif dado < raiz.dado: 
            raiz.esquerda = self._inserir_recursivamente(raiz.esquerda, dado)
        else:
            raiz.direita = self._inserir_recursivamente(raiz.direita, dado)
        return raiz

    def procurar(self,dado):
        return self._procurar_recursivamente(self.raiz, dado)
    
    def _procurar_recursivamente(self,raiz,dado):
        if raiz is None:
            print("Valor não encontrado")
            return None  
        if raiz.dado == dado:
            print("Valor encontrado: ", raiz.dado)
            return raiz
        elif dado < raiz.dado:
            return self._procurar_recursivamente(raiz.esquerda, dado)
        else:
            return self._procurar_recursivamente(raiz.direita, dado)


    def exibir(self):

        def pre_ordem(self):
            self._pre_ordem_recursivamente(self.raiz)

        def _pre_ordem_recursivamente(self, raiz):
            if raiz:
                print(raiz.dado, end=" ")
                self._pre_ordem_recursivamente(raiz.esquerda)
                self._pre_ordem_recursivamente(raiz.direita)

        def em_ordem(self):
            self._em_ordem_recursivamente(self.raiz)

        def _em_ordem_recursivamente(self, raiz):
            if raiz:
                self._em_ordem_recursivamente(raiz.esquerda)
                print(raiz.dado, end=" ")
                self._em_ordem_recursivamente(raiz.direita)

        def pos_ordem(self):
            self._pos_ordem_recursivamente(self.raiz)

        def _pos_ordem_recursivamente(self, raiz):
            if raiz:
                self._pos_ordem_recursivamente(raiz.esquerda)
                self._pos_ordem_recursivamente(raiz.direita)
                print(raiz.dado, end=" ")
    

def main():
    arvore = ArvoreB()

    while True:
        opcao = int(input("\n 1 - Inserir cadastro\n 2 - Procurar por nome \n 3 - Exibir cadastros\n"))
        if opcao == 1:
            chave = int(input("Digite o numero: "))
            nome = input("Digite seu nome: ")
            rg = int(input("Digite seu RG: "))
            fone = int(input("Digite seu número de telefone: "))
            arvore.inserir(chave)
        elif opcao == 2:
            num = int(input("Qual nome deseja procurar? "))
            arvore.procurar(num)
        elif opcao == 3:
            arvore.exibir()

main()