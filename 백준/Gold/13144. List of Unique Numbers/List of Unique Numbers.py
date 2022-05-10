def solution():
    N = int(input())
    G = list(map(int, input().split()))

    NUM = [0] * 100100
    NUM[G[0]] = 1
    result = 0
    L = 0
    R = 0

    while True:
        if R+1 == N:
            break
        if NUM[G[R+1]] == 1: # Stop the moving of R
            result += R-L+1
            NUM[G[L]] = 0
            L += 1
        else:
            R += 1
            NUM[G[R]] = 1
    while L < N:
        result += N-L
        L += 1
    print(result)


if __name__ == '__main__':
    solution()
