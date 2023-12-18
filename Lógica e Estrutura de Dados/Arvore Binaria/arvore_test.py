from collections import deque

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def inserir(self, valor):
        self.raiz = self._inserir(self.raiz, valor)

    def _inserir(self, no, valor):
        if no is None:
            return No(valor)
        if valor == no.valor:
            print("Número duplicado. Não será inserido.")
            return no

        elif valor < no.valor:
            no.esquerda = self._inserir(no.esquerda, valor)
        else:
            no.direita = self._inserir(no.direita, valor)
        return no

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, no, valor):
        if no is None or no.valor == valor:
            return no
        if valor < no.valor:
            return self._buscar(no.esquerda, valor)
        return self._buscar(no.direita, valor)

    def remover(self, valor):
        self.raiz = self._remover(self.raiz, valor)

    def _remover(self, no, valor):
        if no is None:
            return no

        if valor < no.valor:
            no.esquerda = self._remover(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._remover(no.direita, valor)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda

            no.valor = self._min_valor(no.direita)
            no.direita = self._remover(no.direita, no.valor)

        return no

    def _min_valor(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no.valor

    def imprimir_em_ordem(self):
        self._imprimir_em_ordem(self.raiz)
        print()

    def _imprimir_em_ordem(self, no):
        if no:
            self._imprimir_em_ordem(no.esquerda)
            print(no.valor, end=' ')
            self._imprimir_em_ordem(no.direita)

    def imprimir_pre_ordem(self):
        self._imprimir_pre_ordem(self.raiz)
        print()

    def _imprimir_pre_ordem(self, no):
        if no:
            print(no.valor, end=' ')
            self._imprimir_pre_ordem(no.esquerda)
            self._imprimir_pre_ordem(no.direita)

    def imprimir_pos_ordem(self):
        self._imprimir_pos_ordem(self.raiz)
        print()

    def _imprimir_pos_ordem(self, no):
        if no:
            self._imprimir_pos_ordem(no.esquerda)
            self._imprimir_pos_ordem(no.direita)
            print(no.valor, end=' ')

    def imprimir_em_nivel(self):
        if self.raiz is None:
            return

        fila = deque([self.raiz])

        while fila:
            no = fila.popleft()
            print(no.valor, end=' ')

            if no.esquerda:
                fila.append(no.esquerda)
            if no.direita:
                fila.append(no.direita)

arvore = ArvoreBinaria()
arvore.inserir(5)
arvore.inserir(3)
arvore.inserir(7)
arvore.inserir(1)
arvore.inserir(4)

print("Árvore em ordem:")
arvore.imprimir_em_ordem()

print("\nÁrvore em pré-ordem:")
arvore.imprimir_pre_ordem()

print("\nÁrvore em pós-ordem:")
arvore.imprimir_pos_ordem()

print("\nÁrvore em nível:")
arvore.imprimir_em_nivel()

valor_procurado = 4
resultado = arvore.buscar(valor_procurado)

if resultado:
    print(f"\n{valor_procurado} encontrado na árvore.")
else:
    print(f"\n{valor_procurado} não encontrado na árvore.")

valor_remover = 3
arvore.remover(valor_remover)
print(f"\nRemovido o valor {valor_remover}. Árvore em ordem após a remoção:")
arvore.imprimir_em_ordem()
