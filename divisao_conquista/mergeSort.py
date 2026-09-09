import random

lista = [3, 6, 8, 3, 6, 24, 6, 3, 67, 7, 0]

def ordena(l):

    if len(l) == 1 or len(l) == 0:
        return l

    a = ordena(l[:len(l)//2])
    b = ordena(l[len(l)//2:])

    i, j = 0, 0
    resultado = []
    while True:
        if a[i] > b[j]:
            resultado.append(b[j])
            j += 1
        else:
            resultado.append(a[i])
            i += 1

        if i == len(a)-1 or j == len(b)-1:
            break

    


print(ordena(lista))