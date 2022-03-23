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

N, M = map(int, input().split())
graph = [[] for i in range(M)]
for i in range(N):
    text = input()
    for j in range(len(text)):
        graph[i].append(text[j])

for i in graph:
    print(i)

# if the positions of two balls are the same, remove the case.
# directions are not the same as previous direction. ( overlap )
