import sys
def solution():
    num = input()
    N_origin = int(num)
    N = int(num)
    num = list(map(int, num))
    l = len(num)
    d = l // 2
    m = l % 2

    def mk():
        nonlocal N, num, d, m, l
        A = ''.join(map(str, (num[:d]+num[d-1+m::-1])))

        while int(A) <= N_origin:
            N = N + 10**(d-1+m)
            d = l // 2
            m = l % 2
            l = len(num)
            num = list(str(N))
            A = ''.join(map(str, (num[:d] + num[d - 1 + m::-1])))

        print(A)

    mk()

if __name__ == '__main__':
    solution()
