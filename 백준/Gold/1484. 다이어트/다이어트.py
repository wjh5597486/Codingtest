def solution():
    N = int(input())
    left, right = 1, 1
    result = []

    while left < 100000 and right < 100000:
        temp = (left+right)*(left-right)
        if temp == N:
            result.append(left)
        if temp < N:
            left += 1
            continue
        right += 1

    if result:
        for i in result:
            print(i)
    else:
        print(-1)


if __name__ == '__main__':
    solution()
