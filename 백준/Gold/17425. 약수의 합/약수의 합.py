import sys
MAX = 1000001
graph = [1] * MAX
for i in range(2, MAX):
    N = i
    while N < MAX:
        graph[N] += i
        N += i
        
def solution():

    for i in range(2, MAX):
        graph[i] += graph[i - 1]

    for _ in range(int(input())):
        print(graph[int(sys.stdin.readline())])

if __name__ == "__main__":
    solution()
