def solution():
    N = int(input())
    G = list(map(int, input().split()))
    D = int(input())
    result = []
    while D >= len(G):
        if G==[]:
            break
        j = G.index(max(G[:]))
        result.append(G.pop(j))
        D -= j
    while D > 0:
        if G==[]:
            break
        j = G.index(max(G[:D+1]))
        result.append(G.pop(j))
        D -= j

    result += G
    print(*result)


if __name__ == "__main__":
    solution()