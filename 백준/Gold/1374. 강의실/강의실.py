import sys
def solution():
    N = int(input())
    start = []
    end = []
    for i in range(N):
        A, S, E = map(int, sys.stdin.readline().split())
        start.append(S)
        end.append(E)
    start.sort()
    end.sort()

    s = 1
    e = 0

    num_class = 1
    result = 1
    while s < N:
        if start[s] < end[e]:
            s += 1
            num_class += 1
        else:
            e += 1
            num_class -= 1

        result = max(result, num_class)
    print(result)

if __name__ == '__main__':
    solution()
