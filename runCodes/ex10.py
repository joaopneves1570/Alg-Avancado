import heapq

def ordenacaoTopologica(n, lista_adj, nomes, graus):
    topo = []
    q = []

    for i in range(n):
        if graus[i] == 0:
            heapq.heappush(q, (nomes[i], i))

    while q:
        u = heapq.heappop(q)[1]
        topo.append(u)

        for v in lista_adj[u]:
            graus[v] -= 1
            if graus[v] == 0:
                heapq.heappush(q, (nomes[v], v))

    return topo if len(topo) == n else None

def main():
    n = int(input())

    bebidas = {}
    lista_adj = []
    nomes = [None] * n
    graus = [0] * n
    for i in range(n):
        lista_adj.append([])
        bebida = input()
        bebidas[bebida] = i
        nomes[i] = bebida


    # print(bebidas)
    # print(lista_adj)
    # print(graus)

    m = int(input())

    for i in range(m):
        relacao = input().split()
        anterior = relacao[0]
        proxima = relacao[1]

        lista_adj[bebidas[anterior]].append(bebidas[proxima])
        graus[bebidas[proxima]] += 1

    # print(lista_adj)

    respostas = ordenacaoTopologica(n, lista_adj, nomes, graus)

    # print(respostas)
    print(' '.join([nomes[i] for i in respostas]) + '.')
    

    


if __name__ == '__main__':
    main()