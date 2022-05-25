def solution():
    N = int(input())
    if N%2 != 0:
        print(0)
    else:
        G = [1]
        for i in range(2, N+1, 2):
            G.append(G[-1]*3)
            for k in range(4, i+1,2):
                G[-1] += G[k//2-2]*2
        print(G[-1])





if __name__ == "__main__":
    solution()

