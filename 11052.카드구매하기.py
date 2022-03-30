N = int(input())
graph = [0] + list(map(int, input().split()))
A = [0] * (N+1)
for i in range(1,N+1):
    for j in range(1, i+1):
        A[i] = max(A[i], A[i-j] + graph[j])
print(A[-1])
