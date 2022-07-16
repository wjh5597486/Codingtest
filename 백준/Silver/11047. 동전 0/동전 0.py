from collections import deque

def solution():
    N, K = map(int, input().split())
    G = [int(input()) for i in range(N)]
    G.sort(reverse=True)
    cnt = 0
    for i in G:
        cnt += K // i
        K = K % i
    print(cnt)



if __name__ == '__main__':
    solution()
