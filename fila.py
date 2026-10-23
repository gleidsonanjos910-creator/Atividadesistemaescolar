
from ED.node import Node


class Fila():

    def __init__(self):
        self.inicio = None
        self.final = None

    def esta_vazia(self):
        return self.inicio is None

    def enqueue(self, dado):
        novo = Node(dado)

        if not self.esta_vazia():
            self.final.prox = novo
            self.final = novo
        else:
            self.inicio = novo
            self.final = novo

    def dequeue(self):
        if self.esta_vazia():
            return None

        aux = self.inicio
        dado = aux.item

        self.inicio = self.inicio.prox

        if self.inicio is None:
            self.final = None

        del aux
        return dado

    def first(self):
        if not self.esta_vazia():
            return self.inicio.item
        return None

    def destruir(self):
        while not self.esta_vazia():
            self.dequeue()

    # 1. Imprimir a fila sem alterar sua ordem
    def imprimir_fila(self):
        aux = self.inicio

        print("INÍCIO -> ", end="")

        while aux:
            print(aux.item, end=" -> ")
            aux = aux.prox

        print("FIM")

    # Mantém compatibilidade com seu método original
    def imprimir(self):
        self.imprimir_fila()

    # 2. Buscar um elemento
    def buscar(self, info):
        aux = self.inicio

        while aux:
            if aux.item == info:
                return True
            aux = aux.prox

        return False

    # 3. Editar um elemento
    def editar(self, info, novo_dado=None):
        aux = self.inicio

        while aux:
            if aux.item == info:
                if novo_dado is None:
                    novo_dado = input("Digite o novo valor: ")

                aux.item = novo_dado
                return True

            aux = aux.prox

        return False

    # 4. Remover um elemento específico
    def remover(self, info):
        anterior = None
        atual = self.inicio

        while atual:
            if atual.item == info:

                if anterior is None:
                    self.inicio = atual.prox
                else:
                    anterior.prox = atual.prox

                if atual == self.final:
                    self.final = anterior

                del atual
                return True

            anterior = atual
            atual = atual.prox

        return False

    # 5. Remover elementos repetidos
    def remover_repetidos(self):
        atual = self.inicio

        while atual:
            anterior = atual
            proximo = atual.prox

            while proximo:
                if proximo.item == atual.item:
                    anterior.prox = proximo.prox

                    if proximo == self.final:
                        self.final = anterior

                    proximo = anterior.prox
                else:
                    anterior = proximo
                    proximo = proximo.prox

            atual = atual.prox
