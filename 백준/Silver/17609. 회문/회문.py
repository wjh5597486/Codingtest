def solution():
    def check(L, R):
        while L < R:
            if G[L] != G[R]:
                return 0
            L += 1
            R -= 1
        return 1

    for i in range(int(input())):
        G = input()
        R = len(G) - 1
        L = 0
        result = 0
        while L < R:
            if G[L] != G[R]:
                if check(L+1,R) or check(L,R-1):
                    result = 1
                else:
                    result = 2
                break
            L += 1
            R -= 1
        print(result)



if __name__ == '__main__':
    solution()
