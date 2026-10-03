def escolheRoupa(m, itens, cupom, limite):
    orcamentos = [-1]*(m+cupom+1)
    orcamentos[0] = 0

    for item in itens:
        precoItem = item[0]
        satisfacaoItem = item[1]

        for orcamento in range(len(orcamentos) - 1, precoItem - 1, -1):
            if orcamentos[orcamento - precoItem] != -1:
                orcamentos[orcamento] = max(orcamentos[orcamento], orcamentos[orcamento - precoItem] + satisfacaoItem)

    return max(orcamentos[c] for c in range(len(orcamentos)) if c <= m or (c > limite and c <= (m+cupom)))          

def main():

    c = int(input())

    for i in range(c):
        cupom = 200
        limite = 2000
        entradas = [int(x) for x in input().split()]
        n = entradas[0]
        m = entradas[1]
        itens = []

        for i in range(n):
            item = [int(x) for x in input().split()]
            itens.append(item)

        print(escolheRoupa(m, itens, cupom, limite))



if __name__ == '__main__':
    main()