import random

lista = [3, 6, 8, 3, 6, 24, 6, 3, 67, 7, 0]

def ordena(l):

    if len(l) == 1 or len(l) == 0:
        return l

    sorteado = random.randint(0, len(l)-1)
    esquerda = [x for i, x in enumerate(l) if x < l[sorteado] and i != sorteado]
    direita = [x for i, x in enumerate(l) if x >= l[sorteado] and i != sorteado]

    esquerda = ordena(esquerda)
    direita = ordena(direita)

    return esquerda + [l[sorteado]] + direita

print(ordena(lista))