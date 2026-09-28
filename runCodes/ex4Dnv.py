def kadane(vetor, n):
    melhor = [0] * n
    melhor[0] = vetor[0]
    for i in range(1, n):
        melhor[i] = max(vetor[i], melhor[i-1]+ vetor[i])

    return max(melhor)

def main():
    n = int(input())

    matriz = []
    for i in range(n):
        matriz.append([int(x) for x in input().split()])

    melhor = matriz[0][0]
    for idx_linha_top in range(n):
        vetor = [0] * n

        for linha_bottom in matriz[idx_linha_top:]:
            atual = 0
            for j in range(n):
                vetor[j] += linha_bottom[j]
                x = vetor[j]
                if j == 0:
                    atual = x
                else:
                    atual = max(x, atual + x)
                
                melhor = max(atual, melhor)
        


    print(melhor)



if __name__ == "__main__":
    main()