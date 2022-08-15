def solution():
    c = 1
    for i in range(3):
        c *= int(input())
    c = list(str(c))

    for i in range(10):
        print(c.count(str(i)))

if __name__ == '__main__':
    solution()
