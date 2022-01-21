N = []
times = int(input())
for i in range(times):
  N.append(list(map(int,input().split())))

for n in range(1,len(N)):
  N[n][n] += N[n-1][-1]
  N[n][0] += N[n-1][0]
  for i in range(1,n):  
    N[n][i] += max(N[n-1][i-1], N[n-1][i])

print(max(N[-1]))
