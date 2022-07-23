def solution():
    A = input()
    B = input()

    C = len(A)
    R = len(B)
    G = [[0] * (C+1) for i in range(R+1)]

    for r in range(1, R+1):
        for c in range(1, C+1):
            if A[c-1] == B[r-1]:
                G[r][c] = G[r-1][c-1] + 1
            else:
                G[r][c] = max(G[r-1][c], G[r][c-1])

    result = ""
    r, c = R, C
    while r !=0 and c !=0:
        if A[c-1] == B[r-1]:
            result += A[c-1]
            r -= 1
            c -= 1
        elif r>0:
            if G[r-1][c] == G[r][c]:
                r -= 1
            elif G[r][c-1] == G[r][c]:
                c -= 1
            else:
                if r > 0:
                    r -= 1
                else:
                    c -= 1

    print(len(result))
    if len(result) != 0:
        print(result[::-1])


if __name__ == '__main__':
    solution()
