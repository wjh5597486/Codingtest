def solution():
    G = input()
    string = list(input())

    dic = dict()
    for idx, s in enumerate(G):
        dic[s] = idx+1
    N = len(G)
    result = dic[string[-1]]
    K = N
    for i in range(1,len(string)):
        t = string[-(i+1)]
        result += dic[t] * K
        K *= N
        K %= 900528
        result %= 900528

    print(result)


if __name__ == '__main__':
    solution()
