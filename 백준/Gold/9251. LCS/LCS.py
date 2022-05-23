import sys
def solution():
    A = input()
    B = input()
    r, c = len(A), len(B)
    G = [[0]*(c+1) for _ in range(r+1)]

    for i in range(1,r+1):
        for j in range(1,c+1):
            if A[i-1] == B[j-1]:
                G[i][j] = G[i-1][j-1] + 1
            else:
                G[i][j] = max(G[i-1][j], G[i][j-1])

    print(G[-1][-1])




if __name__ == "__main__":
    solution()

