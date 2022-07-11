import math

def solution():

    N, M = map(int, input().split())

    num_list = [0] * 1_000_001

    nums = []

    for i in range(2, int(math.sqrt(M))+1):
        if num_list[i] == 1:
            continue
        n = i*i
        if n <= M:
            nums.append(n)
            for j in range(i,len(num_list),i):
                num_list[j] = 1

    result = [1] * (M-N+1)

    for num in nums:
        a = N // num
        b = N % num
        min_num = a * num if b == 0 else (a+1) * num
        for idx in range(min_num, M+1, num):
             result[idx-N] = 0

    print(sum(result))


if __name__ == '__main__':
    solution()
