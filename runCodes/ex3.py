def greedy(n, p, q, pesoOvos):

    pesoAtual = 0
    nrOvos = 0

    for i in range(n):
        menorPeso = min(pesoOvos)

        if pesoAtual + menorPeso <= q and nrOvos + 1 <= p:
            pesoAtual += menorPeso
            nrOvos += 1
            pesoOvos.remove(menorPeso)

    return nrOvos


def main():

    t = int(input())

    for i in range(t):
        entrada = input().split()
        n, p, q = int(entrada[0]), int(entrada[1]), int(entrada[2])

        pesoOvos = [int(x) for x in input().split()]

        resultado = greedy(n, p, q, pesoOvos)

        print(f'Caso {i+1}: {resultado}')
    




if __name__ == "__main__":
    main()
