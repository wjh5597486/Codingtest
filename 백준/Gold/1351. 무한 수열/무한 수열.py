def solution():
    N, P, Q = map(int, input().split())
    dic = {0:1}

    def call(n):
        if n in dic:
            return dic[n]
        else:
            dic[n] = call(n//P) + call(n//Q)
            return dic[n]

    print(call(N))

if __name__ == '__main__':
    solution()