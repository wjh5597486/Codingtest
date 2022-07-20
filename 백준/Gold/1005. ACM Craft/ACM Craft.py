import heapq
def solution():
    for i in range(int(input())):
        num_build, num_rule = map(int, input().split())
        time_build = [0] + list(map(int, input().split()))
        next_build = dict()
        need_build = dict()
        for i in range(1, num_build+1):
            need_build[i] = []
        start_build = set(range(1,num_build+1))

        for i in range(num_rule):
            a, b = map(int, input().split())
            need_build[b].append(a)
            if next_build.get(a) == None:
                next_build[a] = [b]
            else:
                next_build[a].append(b)

            if b in start_build:
                start_build.discard(b)
        last_build = int(input())

        fin_build = [0] * (num_build+1)
        hq = []
        for idx in start_build:
            heapq.heappush(hq,(time_build[idx],idx))

        def check_need(idx):
            for need in need_build[idx]:
                if fin_build[need] == 0:
                    return False
            return True

        while hq:
            cur_time, cur_build = heapq.heappop(hq)
            fin_build[cur_build] = True

            if cur_build == last_build:
                print(cur_time)
                break

            if next_build.get(cur_build):
                for nxt in next_build[cur_build]:
                    if check_need(nxt):
                        heapq.heappush(hq, (cur_time+time_build[nxt], nxt))


if __name__ == '__main__':
    solution()
