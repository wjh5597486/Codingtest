def solution():
    G = list(map(str, range(10)))
    # 1. 계속 붙여도 어차피 중복은 안 생긴다. 다 만들고 소트
    N = int(input())
    try:
        for i in range(500000):
            for j in range(int(G[i][0])+1, 10):
                G.append(str(j) + G[i])
    except:
        G = list(map(int, G))
        G.sort()
        try:
            print(int(G[N]))
        except:
            print(-1)


if __name__ == "__main__":
    solution()
