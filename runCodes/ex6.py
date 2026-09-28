from bisect import bisect_left, bisect_right

def main():

    n = int(input())

    for i in range(n):

        entradas = [int(x) for x in input().split()]
        p, c = entradas[0], entradas[1]
        aventureiros = [int(x) for x in input().split()]
        comerciantes = [int(x) for x in input().split()]

        aventureiros.sort()
        comerciantes.sort()

        melhor_x = 0
        melhor_total = float('inf')

        for x in ([0] + aventureiros):
            total =  p - bisect_right(aventureiros, x) + bisect_left(comerciantes, x)
            if total < melhor_total:
                melhor_x = x
                melhor_total = total

        print(melhor_x, melhor_total)



if __name__ == '__main__':
    main()