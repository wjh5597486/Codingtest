from math import comb
def solution():
    for i in range(int(input())):
        b, a = map(int, input().split())
        print(comb(a,b))

if __name__ == '__main__':
    solution()
