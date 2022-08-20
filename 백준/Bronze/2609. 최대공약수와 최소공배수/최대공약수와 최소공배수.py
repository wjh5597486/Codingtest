import math
def solution():
    a, b = map(int, input().split())
    print(math.gcd(a,b))
    print(math.lcm(a,b))



if __name__ == '__main__':
    solution()
