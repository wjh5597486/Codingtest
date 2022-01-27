from collections import deque

N, M = map(int, input().split())
FIN = [N, M]
maze = []
for i in range(N):
  maze.append(list(map(int, input())))
  

dq = deque()
dq.append([0,0])

while maze[-1][-1] == 1:
  y, x = dq.popleft()

  for yi, xi in [[y+1,x], [y,x+1],[y-1,x],[y,x-1]]:
 
    if not(0 <= yi < N and 0 <= xi < M):
      continue
    if maze[yi][xi] != 1:
      continue

    dq.append([yi, xi])
    maze[yi][xi] = maze[y][x] +1

print(maze[-1][-1])