

def probability(num, total, times):
    result = 1
    for i in range(times):
        if num-i <= 0:
            return 0
        result *= (num-i)/(total-i)
    return result

M = int(input())
N = list(map(int, input().split()))
K = int(input())
# M = 2
# N = [5,6,7]
# K = 2

total_num = sum(N)

answer = 0

for num in N:
    answer += probability(num, total_num, K)
print(answer)

