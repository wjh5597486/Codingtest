def solution():
    N = int(input())
    dice = list(map(int, input().split()))
    max2 = [(0, 1), (0, 2), (0, 3), (0, 4),(1, 2), (1, 3), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
    max3 = [(0, 1, 2), (0, 1, 3), (0, 2, 4), (0, 3, 4), (1, 2, 5), (1, 3, 5), (2, 4, 5), (3, 4, 5)]
    max1 = min(dice)
    max2 = min(sum(dice[j] for j in i) for i in max2)
    max3 = min(sum(dice[j] for j in i) for i in max3)

    if N == 1:
        result = sum(dice)-max(dice)
    else:
        result = max1 * ((N - 1) * (N - 2) * 4 + (N - 2) ** 2) \
                 + max2 * 4 * ((N - 1) + (N - 2)) \
                 + max3 * 4 * (N != 1)
    print(result)

if __name__ == "__main__":
    solution()
