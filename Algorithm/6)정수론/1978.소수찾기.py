def prime(n):
    if n == 2:
        return 1
    if n % 2 == 0 or n == 1:
        return 0
    for i in range(3,n,2):
        if n % i == 0:
            return 0
    return 1

M = input()
N = list(map(int,input().split()))

result = 0

for x in N:
    result += prime(x)
print(result)