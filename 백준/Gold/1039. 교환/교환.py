def solution():
    N, M = map(int, input().split())
    S = set([N])

    def suffle(S):
        R = set()
        while S:
            x = list(str(S.pop()))
            for i in range(len(x)-1):
                for j in range(i+1, len(x)):
                    line = [a for a in x]
                    line[i], line[j] = line[j], line[i]
                    if line[0] == '0':
                        continue
                    T = ''
                    for t in line:
                        T += t
                    R.add(T)
        return R

    for i in range(M):
        S = suffle(S)

    if S:
        print(max(S))
    else:
        print(-1)

if __name__ == "__main__":
    solution()