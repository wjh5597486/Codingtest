import math

def solution():
    def search(start, end):
        result = 0

        while start <= end:
            mid = (start + end) // 2
            cur = G[0]
            cnt = 1

            for i in range(1, N):
                if G[i] >= cur + mid:
                    cur = G[i]
                    cnt += 1


            if cnt >= C:
                start = mid + 1
                result = mid
            else:
                end = mid - 1

        return result

    N, C = map(int, input().split())
    G = sorted(int(input()) for i in range(N))
    start = 1
    end = G[-1] - G[0]

    print(search(start, end))




if __name__ == '__main__':
    solution()
