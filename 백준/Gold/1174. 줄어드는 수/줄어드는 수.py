def solution():
    N = int(input())-1
    G = list(range(0, 10))

    for i in range(1_000_000):
        if i >= len(G):
            G.sort()
            break
        str_num = str(G[i])
        first_num = int(str_num[0])

        for j in range(first_num + 1 , 10):
            next_num = int(str(j) + str_num)
            G.append(next_num)

    if N >= len(G):
        print(-1)

    else:
        print(G[N])

if __name__ == "__main__":
    solution()