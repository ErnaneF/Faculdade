class Nodo:
    def __init__(self, dado):
        self.dado = dado
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
    
    def excluir(self,dado):
        self._excluir_recursivamente(self.raiz,dado)
    
    def _excluir_recursivamente(self, raiz, dado):
        if raiz is None:
            print("Valor não encontrado. ")
            return raiz
        if dado < raiz.dado:
            raiz.esquerda = self._excluir_recursivamente(raiz.esquerda,dado)
        elif dado > raiz.dado:
            raiz.direita = self._excluir_recursivamente(raiz.direita, dado)
        else:
            print("Valor excluído: ", raiz.dado)
            if raiz.esquerda is None:
                return raiz.direita
            elif raiz.direita is None:
                return raiz.esquerda
            raiz.dado = self._minimo_valor_nodo(raiz.direita)
            raiz.direita = self._excluir_recursivamente(raiz.direita, raiz.dado)
        return raiz
    
    def _minimo_valor_nodo(self,raiz):
        atual = raiz
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual.dado
    
    def _maximo_valor_nodo(self,raiz):
        atual = raiz
        while atual.direita is not None:
            atual = atual.direita
        return atual.dado
    
    def exibir_arvore(self):
            self._exibir_arvore_recursivamente(self.raiz, 0)

    def _exibir_arvore_recursivamente(self, raiz, nivel):
        if raiz is not None:
            self._exibir_arvore_recursivamente(raiz.direita, nivel + 1)
            print("  " * nivel + str(raiz.dado))
            self._exibir_arvore_recursivamente(raiz.esquerda, nivel + 1)

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
    

    def em_nivel(self):
        if self.raiz is None:
            print("Árvore vazia.")
            return

        fila = [self.raiz]

        while fila:
            no = fila.pop(0)
            print(no.dado, end=" ")

            if no.esquerda:
                fila.append(no.esquerda)
            if no.direita:
                fila.append(no.direita)
def main():
    arvore = ArvoreB()

    while True:
        opcao = int(input("\n 1 - Inserir\n 2 - Procurar\n 3 - Excluir\n 4 - Para exibir toda a árvore\n 5 - Para mostrar em ordem\n 6 - Para mostrar em pré ordem\n 7 - Para mostrar em pós ordem\n 8 - Para mostrar o em nível\n 9 - para sair\n Digite a opção: "))

        if opcao == 1:
            num = int(input("Digite o numero: "))
            arvore.inserir(num)
        elif opcao == 2:
            num = int(input("Qual número deseja procurar? "))
            arvore.procurar(num)
        elif opcao == 3:
            num = int(input("Digite o número que deseja excluir: "))
            arvore.excluir(num)
        elif opcao == 4:
            arvore.exibir_arvore()
        elif opcao == 5:
            arvore.pre_ordem()
        elif opcao == 6:
            arvore.em_ordem()
        elif opcao == 7:
            arvore.pos_ordem()
        elif opcao == 8:
            arvore.em_nivel()
        elif opcao == 9:
            print("Encerrando")
            break
        else:
            print("Número inválido")
main()