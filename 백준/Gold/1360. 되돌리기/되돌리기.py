def solution():
    N = int(input())
    G = []
    for i in range(N):
        G.append(input().split())
    G.reverse()

    graph = [1] * N

    for i in range(N):
        com, string, time = G[i]
        if com == 'undo' and graph[i] == 1:
            back_time = int(time) - int(string)
            for j in range(i+1, N):
                com2, string2, time2 = G[j]
                if int(time2) >= back_time:
                    graph[j] *= -1
                else:
                    break

    result = ''
    for i in range(N-1,-1,-1):
        if graph[i] == 1 and G[i][0] == 'type':
            result += G[i][1]
    print(result)

if __name__ == '__main__':
    solution()