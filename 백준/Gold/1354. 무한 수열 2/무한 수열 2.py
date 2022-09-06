def solution():
    N, P, Q, X, Y = map(int, input().split())
    A = {0: 1}

    def R(idx):
        if idx <= 0:
            return 1
        if A.get(idx) == None:
            A[idx] = R(idx//P-X) + R(idx//Q-Y)
        return A[idx]

    print(R(N))




if __name__ == "__main__":
    solution()
