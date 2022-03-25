
# N, M = 6,0
# graph = [1,1,9,1,1,1]  #I want to know 3
# N: the number of documents, M: the number of target


T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    graph = list(map(int, input().split()))

    start = 0
    call_stack = 0
    while True:
        call_number = graph[start]
        if call_number == max(graph):
            graph[start] = 0
            call_stack += 1
            if start == M:
                print(call_stack)
                break
        if start == N-1:
            start = 0
        else:
            start += 1



