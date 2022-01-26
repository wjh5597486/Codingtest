
from collections import deque

dq = deque()
dq.append(0)
dq.append(1)
dq.append(1)

print(dq)
N = 1518

for i in range(N-3):
    N -= 1
    x = dq.popleft() * 2
    y = dq[0] * 2
    dq.append((x + y + 1) )

print(dq)
print(dq[N-1])



