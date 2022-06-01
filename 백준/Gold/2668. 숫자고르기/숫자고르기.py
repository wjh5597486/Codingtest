import sys
def solution():
    N = int(input())
    G = []
    for i in range(N):
        G.append(int(input()))

    result = []
    for n, x in enumerate(G):
        N = n+1
        if N == x:
            result.append(N)
        elif N not in result:
            set_up = set([N])
            set_down = set([x])
            next_num = x
            while True:
                if next_num in set_up:
                    break
                set_up.add(next_num)
                next_num = G[next_num-1]
                if next_num in set_down:
                    break
                set_down.add(next_num)
            if set_up == set_down:
                for i in set_up:
                    result.append(i)

    result.sort()
    print(len(result))
    for i in result:
        print(i)


if __name__ == "__main__":
    solution()


