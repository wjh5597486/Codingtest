def solution():
    N, M = map(int, input().split())
    G = list(map(int, input().split()))
    left = []
    right = []
    for i in G:
        if i < 0:
            left.append(-i)
        else:
            right.append(i)

    left.sort()
    right.sort()
    result = []

    left_max = max(left) if left else 0
    right_max = max(right) if right else 0

    def poppop(LIST):
        while LIST:
            result.append(LIST[-1]*2)
            for i in range(M):
                if LIST:
                    LIST.pop()
    poppop(left)
    poppop(right)
    print(sum(result)-max(left_max,right_max))

if __name__ == '__main__':
    solution()