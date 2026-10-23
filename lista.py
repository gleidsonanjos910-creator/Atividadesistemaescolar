
from ED.node import Node


class Lista:
    """
    Implementação de lista simplesmente encadeada.
    """

    def __init__(self):
        self.cabeca = None

    def esta_vazia(self):
        return self.cabeca is None

    def inserir_inicio(self, dado: any):
        novo = Node(dado)
        novo.prox = self.cabeca
        self.cabeca = novo

    def imprimir_lista(self):
        aux = self.cabeca

        while aux:
            print(f">>\n{str(aux)}\n", end="")
            aux = aux.prox

        print("<<")

    def __str__(self):
        aux = self.cabeca
        txt = ""

        while aux:
            txt += f">>\n{str(aux)}\n"
            aux = aux.prox

        return txt + "<<"

    def remover_inicio(self):
        if not self.esta_vazia():
            aux = self.cabeca
            self.cabeca = self.cabeca.prox
            del aux

    def inserir_final(self, dado):
        novo = Node(dado)

        if not self.esta_vazia():
            aux = self.cabeca

            while aux.prox:
                aux = aux.prox

            aux.prox = novo
        else:
            self.cabeca = novo

    def remover_final(self):
        if self.esta_vazia():
            return

        aux = self.cabeca
        ant = None

        while aux.prox:
            ant = aux
            aux = aux.prox

        if ant is not None:
            ant.prox = None
        else:
            self.cabeca = None

    def inserir_ordenado(self, dado):
        novo = Node(dado)

        if self.esta_vazia() or dado <= self.cabeca.item:
            novo.prox = self.cabeca
            self.cabeca = novo
            return

        aux = self.cabeca

        while aux.prox and dado > aux.prox.item:
            aux = aux.prox

        novo.prox = aux.prox
        aux.prox = novo

    def remover_dado(self, dado_busca):
        ant = None
        aux = self.cabeca

        while aux and aux.item != dado_busca:
            ant = aux
            aux = aux.prox

        if aux is None:
            return

        if ant is None:
            self.cabeca = aux.prox
        else:
            ant.prox = aux.prox

    # ==================================
    # MÉTODOS SOLICITADOS NA PROVA
    # ==================================

    def min(self):
        if self.esta_vazia():
            return None

        menor = self.cabeca.item
        aux = self.cabeca.prox

        while aux:
            if aux.item < menor:
                menor = aux.item
            aux = aux.prox

        return menor

    def max(self):
        if self.esta_vazia():
            return None

        maior = self.cabeca.item
        aux = self.cabeca.prox

        while aux:
            if aux.item > maior:
                maior = aux.item
            aux = aux.prox

        return maior

    def sum(self):
        total = 0
        aux = self.cabeca

        while aux:
            total += aux.item
            aux = aux.prox

        return total

    def avg(self):
        quantidade = self.len()

        if quantidade == 0:
            return 0

        return self.sum() / quantidade

    def len(self):
        quantidade = 0
        aux = self.cabeca

        while aux:
            quantidade += 1
            aux = aux.prox

        return quantidade

    def append(self, outra_lista):
        aux = outra_lista.cabeca

        while aux:
            self.inserir_final(aux.item)
            aux = aux.prox

    def reverse(self):
        anterior = None
        atual = self.cabeca

        while atual:
            proximo = atual.prox
            atual.prox = anterior
            anterior = atual
            atual = proximo

        self.cabeca = anterior
