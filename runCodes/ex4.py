def resolve(shows, k):
    def divide(maiorSoma):
        dias = 1
        somaAtual = 0

        for show in shows:
            if somaAtual + show > maiorSoma:
                dias += 1
                somaAtual = show
            else:
                somaAtual += show

        return dias <= k

    menor = max(shows)
    maior = sum(shows)
    res = maior

    while menor <= maior:
        meio = (menor + maior)//2

        if divide(meio):
            res = meio
            maior = meio - 1
        else:
            menor = meio + 1

    return res
        

def main():

    n = int(input())

    for i in range(n):

        entrada = input().split()
        t, k = int(entrada[0]), int(entrada[1])

        duracoes = list(map(int, input().split()))
        
        print(f'Caso {i+1}: {resolve(duracoes, k)}')


if __name__ == "__main__":
    main()