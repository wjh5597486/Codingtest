"""
N: row
M: column
. : blank
# : wall
o : hall
r : red
b : blue

the chances for moving are limited 10 times, then print(-1).
"""

from collections import deque

N, M = map(int, input().split())
graph = [[] for i in range(N)]
for i in range(N):
    text = input()
    for j in range(M):
        graph[i].append(text[j])

for i in graph:
    print(i)

for i in range(N):
    for j in range(M):
        if graph[i][j] == "R":
            red = [i, j]
        if graph[i][j] == "B":
            blue = [i, j]
        if graph[i][j] == "O":
            hole = [i, j]

dq = deque()
dq.append([red, blue, hole])

while dq:
    red1, blu1, hol1 = dq.popleft()



# 4 ways.

# if the positions of two balls are the same, remove the case.
# directions are not the same as previous direction. ( overlap )
