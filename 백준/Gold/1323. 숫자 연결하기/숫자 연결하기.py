def solution():
    N, M = map(int, input().split())

    number = N
    for times in range(1, 1_000_001):
        remainder = number % M

        if remainder == 0:
            print(times)
            return
        else:
            number = int(str(remainder) + str(N))

    print(-1)

if __name__ == "__main__":
    solution()
