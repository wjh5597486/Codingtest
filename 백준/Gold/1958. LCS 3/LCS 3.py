def solution():
    A = list(input())
    B = list(input())
    C = list(input())

    G = [[[0] * (len(A)+1) for _ in range(len(B)+1)] for _ in range(len(C)+1)]

    for c in range(1,len(C)+1):
        for b in range(1,len(B)+1):
            for a in range(1,len(A)+1):
                if A[a-1] == B[b-1] == C[c-1]:
                    G[c][b][a] = G[c-1][b-1][a-1] + 1
                else:
                    G[c][b][a] = max(G[c-1][b][a], G[c][b-1][a], G[c][b][a-1])
    print(G[-1][-1][-1])


if __name__ == '__main__':
    solution()
