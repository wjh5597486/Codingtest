


G = [ int(input()) for i in range(int(input()))]
C = [0, 0, G[0]]
for i in range(1,len(G)):
    C.append(max(C[-3]+C[-1],C[-3]+C[-1]))
print(C[-1])
