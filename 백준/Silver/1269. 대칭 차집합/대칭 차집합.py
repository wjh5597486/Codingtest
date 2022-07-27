def solution():
    N, M = map(int, input().split())
    G = set(map(int, input().split()))
    P = set(map(int, input().split()))
    print(len(G-P)+len(P-G))


if __name__ == '__main__':
    solution()
