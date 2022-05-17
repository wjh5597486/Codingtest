import sys
def solution():
    A, B, K = map(int, sys.stdin.readline().split())


    def go(A):
        A = str(A)
        result = 0
        for i in A:
            result += int(i) ** K
        return result

    G = [float("inf")] * 10000000
    result = 0
    for i in range(A, B+1):
        graph = [i]
        if G[i] != float("inf"):
            result += 1
            continue

        else:
            while True:
                Next = go(graph[-1])
                if G[Next] != float("inf"): # 리스트 마지막.
                    MIN = min(Next, G[Next])
                    while graph:
                        pop = graph.pop()  # 끝자리
                        MIN = min(MIN, pop)
                        G[pop] = MIN
                    break
                    
                elif Next in graph:
                    idx = graph.index(Next)
                    MIN = min(graph[idx:])

                    for i in graph[idx:]:
                        G[i] = MIN
                    while graph:
                        pop = graph.pop()  # 끝자리
                        MIN = min(MIN, pop)
                        G[pop] = MIN
                    break

                else:
                    graph.append(Next)

    print(sum(G[A:B+1]))

if __name__ == "__main__":
    solution()
