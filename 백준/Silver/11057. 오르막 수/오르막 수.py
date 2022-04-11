N = int(input())

G = [1] * 10

for i in range(1, N):
    F = []
    for x in range(10):
        F.append(sum(G[:x+1]))
    G = F

print(sum(G)%10007)