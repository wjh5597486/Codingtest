def solution():
    N = int(input())
    M = input()
    G = [[M[0], 1]]

    for i in M[1:]:
        if i == G[-1][0]:
            G[-1] = [i, G[-1][1]+1]
        else:
            G.append([i, 1])


    A = set()
    result = 0
    for i in range(len(G)):
        A.add(G[i][0])
        sum = G[i][1]
        for j in range(i+1, len(G)):

            A.add(G[j][0])
            if len(A) > N:
                A = set()
                break

            sum += G[j][1]
        result = max(result, sum)

    print(result)


if __name__ == '__main__':
    solution()