def melhoresVagoes(n, vagoes):
    vagoesCrescentes = [1] * n
    vagoesDecrescentes = [1] * n

    for i in range(n-1, -1, -1):
        for j in range(i + 1, n):
            if vagoes[j] > vagoes[i]:
                vagoesCrescentes[i] = max(vagoesCrescentes[i], vagoesCrescentes[j] + 1)
            elif vagoes[j] < vagoes[i]: 
                vagoesDecrescentes[i] = max(vagoesDecrescentes[i], vagoesDecrescentes[j] + 1)


    maior = 0
    for i in range(n):
        soma = vagoesCrescentes[i] + vagoesDecrescentes[i] - 1
        maior = max(maior, soma)

    return maior


def main():

    casos = int(input())

    for i in range(casos):
        n = int(input())

        vagoes = []

        for j in range(n):
            vagao = int(input())
            vagoes.append(vagao)

        print(melhoresVagoes(n, vagoes))
            

if __name__== "__main__":
    main()