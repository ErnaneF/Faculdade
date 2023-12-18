class Nodo:
    #estrutura para o nodo
    def __init__(self, chave):
        self.chave = chave
        self.altura = 1
        self.esquerda = None
        self.direita = None

class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def inserir_chave(self, chave):
        self.raiz = self.inserir(self.raiz, chave)

    def  altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def balanceamento(nodo):
            if not nodo:
                return 0
            return self.altura(nodo.direita) - s
            lf.altura(nodo.esquerda)

    def inserir(self, raiz, chave):
        if not raiz:
            return Nodo(chave) #Verifica se ja existe uma raiz
        
        if chave < raiz.chave:
            raiz.esquerda = self.inserir(raiz, chave) #Vereficia se a chave (número novo) é menor que a raiz já existente
        
        elif chave > raiz.chave:
            raiz.direita = self.inserir(raiz, chave) #Vereficia se a chave (número novo) é maior que a raiz já existente

        else:
            return raiz #Só será utilizado quando o número inserido já existir dentro da árvore


        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita)) # ele vai pegar o maior nível (último nível) e adicionar +1 === nova chave com novo nível

        balanceamento = self.balanceamento(raiz) 

        #Rotação direita-direita
        if balanceamento > 1 and chave < raiz.esquerda.chave:
            return self.rotacao_direita(raiz)
        
        #Rotação esquerda-esquerda
        if balanceamento < -1 and chave > raiz.direita.chave:
            return self.rotacao_esquerda(raiz)
        
        #Rotação direita-esquerda
        if balanceamento > 1 and chave > raiz.

        