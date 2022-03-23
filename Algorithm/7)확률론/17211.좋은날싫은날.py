N, M = map(int, input().split())

GG, GB, BG, BB = map(float, input().split())

if M == 0:
    S = [1, 0]
else:
    S = [0, 1]

for i in range(N):
    x, y = S
    S = [x * GG + y * BG, x * GB + y * BB]

for i in S:
    print(int(i * 1000))