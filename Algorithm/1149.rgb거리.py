
n= int(input())
N=[0]*n

for i in range(len(N)):
  N[i] = list(map(int, input().split()))

for i in range(1, len(N)):
  N[i][0] += min(N[i-1][1],N[i-1][2])
  N[i][1] += min(N[i-1][0],N[i-1][2])
  N[i][2] += min(N[i-1][0],N[i-1][1])


print(min(N[-1][0],N[-1][1],N[-1][2]))
