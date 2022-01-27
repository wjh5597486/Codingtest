from collections import deque

N = int(input())

dq = deque()


dq.append([1,0,0])
inf = float("inf")
check = [[inf] * 2000 for i in range(2000)] 
check[1][0] = 0

while True:
  x, copy, number = dq.popleft()
  if x == N:
    print(number)
    break
  
  # Copy
  if x != copy and check[x][x] == inf:
    dq.append([x, x, number + 1])
    check[x][x] == number +1

  for xi in [x+copy, x-1]:
    if 0 <= xi <= 1999 and check[xi][copy] == inf:
      dq.append([xi, copy, number +1 ])
      check[xi][copy] = number +1 
