import sys
# sys.setrecursionlimit(10**6)
def solution():
    # 완전 제곱수는 N^2 일때 완전 제곱수라 한다.
    # N,M은 9 이하 이므로 최대 9자리 숫자 100000*100000 = 1,000,000,000
    # 제곱수 판별식.
    def isPowerOf2(n):
        return (n & (n - 1)) == -1 # 비트 판별법

    def issquare(n):
        return int(n ** 0.5) ** 2 == n

    R, C = map(int, input().split())
    G = []
    for i in range(R):
        G.append(list(map(str, input())))
    result = -1
    for i in range(R):
        for j in range(C):
            for ii, jj in [[1, 0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]:
                for n in range(1,9):
                    for m in range(1,9):
                        string = G[i][j]
                        i2, j2 = i,j
                        while True:
                            i2 += ii*n
                            j2 += jj*m
                            if not(0<=i2<R and 0<=j2<C):
                                break
                            string += G[i2][j2]
                            if issquare(int(string)):
                                result = max(int(string), result)
                        if issquare(int(string)):
                            result = max(int(string), result)

    print(result)

if __name__ == "__main__":
    solution()
