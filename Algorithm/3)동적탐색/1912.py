N = int(input())
array = list(map(int,input().split()))

sum = 0
max_num = 0
for num in array:
    if sum + num < 0:
        sum = 0
    else:
        sum = num + sum
    max_num = max(max_num, sum)
if max_num == 0:
    max_num = max(array)
print(max_num)