def solution():
    def pow(a, b, c):
        if b == 1:
            return a

        if b % 2 == 0:
            return (pow(a, b // 2, c) ** 2) % c
        else:
            return (pow(a, b-1, c) * a) % c

    a, b, c = map(int, input().split())
    print(pow(a, b,c)%c)



if __name__ == '__main__':
    solution()
