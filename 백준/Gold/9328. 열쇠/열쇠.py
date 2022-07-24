import sys
sys.setrecursionlimit(100001)
from collections import deque

def solution():
    for i in range(int(input())):
        R, C = map(int, input().split())
        G = [list(input()) for i in range(R)]
        visit = [[0]*C for i in range(R)]
        bag = set(list(map(lambda x: ord(x)-32, input())))
        dic = {}
        dic[46] = []
        cnt = []

        def first(r, c):
            if 97 <= ord(G[r][c]) <= 122:  # get a Key
                bag.add(ord(G[r][c]) - 32)
                G[r][c] = '.'

            if G[r][c] == "$":
                cnt.append(1)
                G[r][c] = '.'

            if G[r][c] != "*":
                if dic.get(ord(G[r][c])) == None:
                    dic[ord(G[r][c])] = [(r, c)]

                else:
                    dic[ord(G[r][c])].append((r, c))

        for r in [0, R-1]:
            for c in range(C):
                first(r,c)

        for r in range(1,R-1):
            for c in [0,C-1]:
                first(r,c)

        def explore(r,c,bag):
            sw = 0

            q = deque()
            q.append((r,c))

            if G[r][c] == "$":
                G[r][c] = "."
                return True, r, c, 1

            while q:
                r, c = q.popleft()
                for r2, c2 in [[r+1,c],[r,c+1],[r-1,c],[r,c-1]]:
                    if 0<=r2<R and 0<=c2<C:
                        if visit[r2][c2] == 1:
                            continue
                        visit[r2][c2] = 1

                        if G[r2][c2] == ".":
                            visit[r2][c2] = 1
                            q.append((r2,c2))

                        elif G[r2][c2] == "*":
                            continue

                        elif G[r2][c2] == "$":
                            G[r2][c2] = '.'
                            cnt.append(1)
                            q.append((r2,c2))

                        elif 65 <= ord(G[r2][c2]) <= 90:
                            sw = 1
                            if chr(ord(G[r2][c2])) in bag:  # open the door
                                G[r2][c2] = '.'
                                q.append((r2,c2))
                            else:
                                if dic.get(ord(G[r2][c2])) == None:  # can't open the door
                                    dic[ord(G[r2][c2])] = [(r2, c2)]
                                else:
                                    dic[ord(G[r2][c2])].append((r2, c2))

                        elif 97 <= ord(G[r2][c2]) <= 122:  # get a Key
                            sw = 1
                            bag.add(ord(G[r2][c2])-32)
                            G[r2][c2] = '.'
                            q.append((r2, c2))
            if sw == 0:
                return False
            else:
                return True


        ex_list = dic.pop(46)
        for r,c in ex_list:
            explore(r,c,bag)

        while True:
            switch = 0
            for key in list(bag):
                if dic.get(key) != None:
                    for r,c in dic[key]:
                        if explore(r, c, bag):
                            switch = 1
            if switch == 0:
                break
        print(sum(cnt))


if __name__ == '__main__':
    solution()