from math import factorial as f
def solution():
    n, m = map(int, input().split())
    a = f(n) // f(n-m) // f(m)
    print(a)
if __name__ == '__main__':
    solution()
