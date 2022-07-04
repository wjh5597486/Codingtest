def solution():
    graph = [[0] * 16 for i in range(16)]
    for i in range(1001):
        try:
            white, black = map(int, input().split())
            for w in range(15,-1,-1):
                for b in range(15,-1,-1):
                    # 1. white
                    if w != 0:
                        graph[w][b] = max(graph[w][b], graph[w-1][b] + white)
                    # 2. black
                    if b != 0:
                        graph[w][b] = max(graph[w][b], graph[w][b-1] + black)
        except:
            print(graph[15][15])
            break

if __name__ == '__main__':
    solution()
