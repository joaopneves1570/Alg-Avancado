import sys


def acharPrimos(n):
    primos = [True] * (n + 1)
    primos[0] = primos[1] = False
    p = 2
    while p * p <= n:
        if primos[p]:
            for i in range(p * p, n + 1, p):
                primos[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primos[p]]


def precomputar(maxN, K=8):
    primos = acharPrimos(maxN)
    mascara = (1 << (maxN + 1)) - 1

    cnt = [0] * (K + 1)
    cnt[0] = 1
    for p in primos:
        for j in range(K, 0, -1):
            if cnt[j - 1]:
                cnt[j] |= (cnt[j - 1] << p) & mascara

    minimo = [0] * (maxN + 1)
    for s in range(1, maxN + 1):
        for j in range(1, K + 1):
            if (cnt[j] >> s) & 1:
                minimo[s] = j
                break

    return primos, set(primos), minimo


def busca(k, s, i, primos, conjunto):
    m = len(primos)
    if i >= m:
        return None
    if k == 1:
        if s in conjunto and s >= primos[i]:
            return [s]
        return None
    for idx in range(i, m):
        p = primos[idx]
        if p * k > s:
            break
        resto = busca(k - 1, s - p, idx + 1, primos, conjunto)
        if resto is not None:
            return [p] + resto
    return None


def main():
    dados = sys.stdin.read().split()
    casos = int(dados[0])
    entradas = [int(x) for x in dados[1:1 + casos]]
    if not entradas:
        return

    primos, conjunto, minimo = precomputar(max(entradas))

    saida = []
    for n in entradas:
        k = minimo[n]
        if k == 0:
            saida.append("-1")
            continue
        seq = busca(k, n, 0, primos, conjunto)
        saida.append("".join(map(str, seq)) if seq else "-1")

    print("\n".join(saida))


if __name__ == "__main__":
    main()