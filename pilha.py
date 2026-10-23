
from ED.node import Node


class Pilha():

    def __init__(self):
        """Cria a pilha vazia"""
        self.topo = None

    def esta_vazia(self):
        return self.topo is None

    def push(self, dado):
        novo = Node(dado)
        novo.prox = self.topo
        self.topo = novo

    def pop(self):
        if not self.esta_vazia():
            aux = self.topo
            self.topo = self.topo.prox
            dado = aux.item
            del aux
            return dado
        return None

    def top(self):
        if not self.esta_vazia():
            return self.topo.item
        return None

    def destruir(self):
        while not self.esta_vazia():
            self.pop()

    def imprimir(self):
        aux = self.topo

        print("TOPO")
        while aux:
            print(aux.item)
            aux = aux.prox
        print("BASE")

    # 1. Buscar um elemento
    def buscar(self, info):
        aux = self.topo

        while aux:
            if aux.item == info:
                return True
            aux = aux.prox

        return False

    # 2. Editar um elemento
    def editar(self, info, novo_dado=None):
        aux = self.topo

        while aux:
            if aux.item == info:
                if novo_dado is None:
                    novo_dado = input("Digite o novo valor: ")

                aux.item = novo_dado
                return True

            aux = aux.prox

        return False

    # 3. Remover um elemento específico
    def remover(self, info):
        anterior = None
        atual = self.topo

        while atual:
            if atual.item == info:
                if anterior is None:
                    self.topo = atual.prox
                else:
                    anterior.prox = atual.prox

                del atual
                return True

            anterior = atual
            atual = atual.prox

        return False

    # 4. Remover elementos repetidos
    def remover_repetidos(self):
        atual = self.topo

        while atual:
            anterior = atual
            proximo = atual.prox

            while proximo:
                if proximo.item == atual.item:
                    anterior.prox = proximo.prox
                    proximo = anterior.prox
                else:
                    anterior = proximo
                    proximo = proximo.prox

            atual = atual.prox
