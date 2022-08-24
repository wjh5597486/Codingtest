
def solution():
    n = int(input())
    N = int(input())
    l = list(range(N+1))
    l[0] = 0
    l[1] = 0
    for i in range(2, N+1):
        if l[i] == 0:
            continue

        for i2 in range(i+i, N+1,i):
            l[i2] = 0

    a = l[n:N+1]
    sum_ = sum(a)
    if sum_ == 0:
        print(-1)
        return

    print(sum_)

    for i in a:
        if i != 0:
            print(i)
            break




if __name__ == '__main__':
    solution()
