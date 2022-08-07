G = [list(map(int, input().split())) for i in range(int(input()))]
print(round(abs(sum([G[i-1][0]*G[i][1] - G[i-1][1]*G[i][0] for i in range(len(G))]))/2,1))