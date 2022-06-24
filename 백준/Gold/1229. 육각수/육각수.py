INF = 10 ** 9
d = [0, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 2] + [INF] * 1_000_000


def solution():
    n = int(input())
    if n < 13:
        print(d[n])
        return

    hex = [n*(2*n-1) for n in range(1000)]
    for i in range(13, n + 1):
        min_val = INF
        for h in hex:
            if h > i: 
                break
            min_val = min(min_val, d[i - h])
        d[i] = min_val + 1
    print(d[n])


solution()