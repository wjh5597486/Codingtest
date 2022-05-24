import sys
N, H = map(int, sys.stdin.readline().split())
from_top = [0] * (H + 1)  # 종유석
from_bot = [0] * (H + 1)  # 석순

for i in range(N):
    num = int(sys.stdin.readline())
    if i % 2:
        from_top[num] += 1
    else:
        from_bot[H - num + 1] += 1

for i in range(H - 1, 0, -1):
    from_top[i] += from_top[i + 1]

for i in range(1, H + 1):
    from_bot[i] += from_bot[i - 1]

G = [0] * (H + 1)
for i in range(1, H + 1):
    G[i] = from_top[i] + from_bot[i]

G = G[1:]
result = min(G)
print(result, G.count(result))  # 결과 출력