def main():
    m = int(input())

    for i in range(m):
        entradas = [int(x) for x in input().split()]
        pos_iniciais = [int(x) for x in input().split()]
        l = entradas[0]

        tempo_min = 0
        tempo_max = 0

        minimos = []
        maximos = []

        for p in pos_iniciais:
            minimos.append(min(p, l-p))
            maximos.append(max(p, l-p))

        print(max(minimos), max(maximos))


if __name__ == '__main__':
    main()