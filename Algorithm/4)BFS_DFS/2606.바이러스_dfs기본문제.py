from collections import deque

dq = deque()
check = []

arr = [[]]
for i in range(int(input())):
    arr.append([])

for i in range(int(input())):
    [x, y] = list(map(int, input().split()))
    arr[x].append(y)
    arr[y].append(x)

dq.append(1)

while dq:
    index = dq.popleft()
    for i in arr[index]:
        if i not in check:
            dq.append(i)
            check.append(i)

print(len(check) - 1)
