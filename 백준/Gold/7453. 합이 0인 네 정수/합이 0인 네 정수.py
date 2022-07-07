import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    A, B, C, D = [], [], [], []
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)

    dic = {}
    for i in A:
        for j in B:
            if i + j in dic:
                dic[i + j] += 1
            else:
                dic[i + j] = 1

    cnt = 0
    for i in C:
        for j in D:
            if -(i + j) in dic:
                cnt += dic[-(i + j)]

    print(cnt)

solution()
