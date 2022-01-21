N = int(input())
array = [0]*N

for i in range(N):
  array[i] = int(input())

N = max(array)
saves = [0, 1, 2, 4]


for i in range(1,N+1):  # i = 1 2 3 . . . N
  result = 0 
  
  if i > 3:
    for j in range(1, 4): # j = 1,2,3
      result += saves[-j]
    saves.append(result)

for i in array:
  print(saves[i])