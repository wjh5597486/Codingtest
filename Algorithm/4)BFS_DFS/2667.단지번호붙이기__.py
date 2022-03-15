N = int(input())
graph=[]
for i in range(N):
    a = input()
    add = [int(ai) for ai in a]
    graph.append(add)


#중복
cost = [[0] * N for __ in range(N)]


def quest(h,w,cost,num):
    list = [[h,w]]
    cost[h][w] = num

    while list:
        H, W = list.pop()
        for hi, wi in [[H-1,W],[H,W-1],[H+1,W],[H,W+1]]:
            if 0 <= hi < N and 0 <= wi < N and cost[hi][wi]==0:
                if graph[hi][wi] == 1:
                    cost[hi][wi] = num
                    list.append([hi, wi])

number_sets = 0
for h in range(N):
    for w in range(N):
        if graph[h][w] == 1:
            if cost[h][w] == 0:
                number_sets += 1
                quest(h,w,cost,number_sets)


result = [0]* (number_sets+1)
for h in range(N):
    for w in range(N):
        result[ cost[h][w] ] += 1

print(number_sets)
result = result[1::]
result.sort()
for i in result:
    print(i)