
W,H = map(int,input().split())
arr = []
for i in range(H):
  arr.append(list(map(int,input().split())))



checkList = []

arr2=[]
day = 0

for i in range(H):
  for j in range(W):
    if arr[i][j] == 1:
      checkList.append([i,j])

while True:
  while checkList:
    h,w = checkList.pop()

    for hi,wi in [[h+1,w],[h-1,w],[h,w+1],[h,w-1]]:
      if hi < 0 or wi < 0 or hi>=H or wi>=W:
        continue
      if arr[hi][wi] == 0:
        arr2.append([hi,wi])
        arr[hi][wi] = 1

  while arr2:
    checkList.append(arr2.pop())
  
  if arr2==checkList:
    break
    
  day += 1
  # print("day:",day)
  # for i in arr:print(i)

for a in arr:
  if 0 in a: 
    day = -1
    break

print(day)
  
  