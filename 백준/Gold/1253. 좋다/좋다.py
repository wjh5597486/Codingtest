def solution():
    N = int(input())
    G = list(map(int, input().split()))
    G.sort()

    result = 0
    for i, x in enumerate(G):
        nG = G[:i] + G[i+1:]
        left, right = 0, len(G)-2
        while left < right:
            if nG[left] + nG[right] > x:
                right -= 1
            elif nG[left] + nG[right] < x:
                left += 1
            else:
                result += 1
                break

    return result






if __name__ == '__main__':
    print(solution())
