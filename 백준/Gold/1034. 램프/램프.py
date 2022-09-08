N,L=map(int,input().split())
G=[input()for i in' '*N]
c=int(input())
R=G.count('1' * L)if c%2==0else 0
for x in G:
    n=L-sum(map(int,x))
    if n<=c and n%2==c%2:R=max(R,G.count(x))
print(R)