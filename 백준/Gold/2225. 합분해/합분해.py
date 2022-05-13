N, K = map(int, input().split())

G = [1] * (N+1)
for _ in range(K-1):
  for i in range(1, N+1):
    G[i] = (G[i] + G[i-1])%1000000000
print(G[-1])