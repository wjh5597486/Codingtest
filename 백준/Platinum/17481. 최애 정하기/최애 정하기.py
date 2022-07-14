import sys

def solution():
    N, M = map(int, input().split())
    members = dict()
    for i in range(M):
        members[sys.stdin.readline().strip()] = None
    friends = dict()
    for i in range(N):
        friends[i] = list(sys.stdin.readline().split())[1::]


    def dfs(idx):
        if check[idx] == 1:
            return False
        check[idx] = 1
        for name in friends[idx]:
            if members[name] == None or dfs(members[name]):
                members[name] = idx
                return True

        return False

    for i in range(N):
        check = [0] * (N)
        dfs(i)

    cnt = 0
    for i in range(N):
        if i in members.values():
            cnt += 1

    if N == cnt:
        print("YES")
    else:
        print("NO")
        print(cnt)

if __name__ == '__main__':
    solution()