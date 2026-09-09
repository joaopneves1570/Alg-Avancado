def eValido(combinacao, cor, pares):

    parAnalisado = None

    if len(combinacao) >= 1:
        parAnalisado = set([combinacao[-1], cor])
    else:
        return True

    if parAnalisado in pares:
        return False

    return True

def backtracking(cores, combinacao, pares, resultado):

    total = 0

    if len(combinacao) == len(cores):
        resultado.append(combinacao.copy())
        return 1

    for cor in cores:
        if cor in combinacao:
            continue

        if eValido(combinacao, cor, pares):
            combinacao.append(cor)
            total += backtracking(cores, combinacao, pares, resultado)
            combinacao.pop()
        else:
            continue

    return total

def main():
    t = int(input())

    for ts in range(t):

        n = int(input())
        cores = input().split()

        m = int(input())
        pares = []
        for ms in range(m):
            pares.append(set(input().split()))

        combinacao = []
        resultado = []

        print(backtracking(cores, combinacao, pares, resultado))
        print(*resultado[0])

if __name__ == "__main__":
    main()