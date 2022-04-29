# https://www.acmicpc.net/problem/15961
import sys
import heapq

def solution():
    import heapq

    N, M = map(int, input().split())
    arr = []
    LIST = [1] * 1001  # 몇번째 인덱스에 있는 배열을 선택할 건지
    MAX = 0
    hq = []
    for i in range(N):
        li = list(map(int, input().split()))
        li.sort()
        MAX = max(MAX, li[0])
        arr.append(li)
        heapq.heappush(hq, (arr[i][0], i))


    result = float("inf")
    
    while hq:
        MIN, list_num = heapq.heappop(hq)
        result = min(result, MAX - MIN)

        if LIST[list_num] == M:
            break

        heapq.heappush(hq, (arr[list_num][LIST[list_num]], list_num))
        MAX = max(MAX, arr[list_num][LIST[list_num]])
        LIST[list_num] += 1

    print(result)
if __name__ == '__main__':
    solution()
