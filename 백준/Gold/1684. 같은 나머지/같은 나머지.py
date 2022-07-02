from math import gcd
def solution():

    N = int(input())
    G = list(map(int, input().split()))
    min_g = max(map(lambda x: abs(x), G))
    result = 0
    for i in range(0, min_g):
        LIST = list(map(lambda x: x-i, G))
        X = gcd(*LIST)
        result = max(result,  X)
    print(result)

if __name__ == "__main__":
    solution()