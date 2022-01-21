array = [1]*int(input())
nums = list(map(int,input().split()))

for i in range(0,len(nums)):
  for j in range(0,i):
    if nums[i] > nums[j]:
      array[i] = max(array[j] + 1 ,array[i])
print(max(array))