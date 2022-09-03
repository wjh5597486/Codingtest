import sys
def solution():
    N = int(input())
    G = list(map(int, input().split()))
    K = [[0] * (21) for i in range(N)]

    K[0][G[0]] = 1

    for idx, num in enumerate(G[1:-1]):
        for i in range(21-num):
            K[idx+1][i+num] += K[idx][i]
        for i in range(num, 21):
            K[idx+1][i-num] += K[idx][i]

    print(K[-2][G[-1]])



if __name__ == '__main__':
    solution()
