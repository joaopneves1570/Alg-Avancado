nCasos = int(input())

for i in range(nCasos):

    x = 0
    nInstrucoes = int(input())
    instrucoes = {}

    for j in range(nInstrucoes):
        instrucao = input().split()
        if instrucao[0] == 'ESQUERDA':
            x -= 1
            instrucoes[j] = -1
            continue
        if instrucao[0] == 'DIREITA':
            x += 1
            instrucoes[j] = 1
            continue
        
        instrucaoRepetida = instrucoes[int(instrucao[1])]
        instrucoes[j] = instrucaoRepetida
        x += instrucaoRepetida
        

    print(x)