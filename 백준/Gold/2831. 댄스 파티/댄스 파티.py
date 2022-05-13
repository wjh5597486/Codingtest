import sys


def solution():
    N = int(input())
    M = list(map(int, sys.stdin.readline().split()))
    W = list(map(int, sys.stdin.readline().split()))

    M.sort()
    W.sort()
    W.reverse()
    L = 0  # for man
    R = 0  # for womanS
    result = 0
    while R < N and L < N:
        if M[L] < 0:  # 남자가 음수 일때
            if W[R] < 0: # 여자도 음수면 다음 남자로
                L += 1
            elif W[R] + M[L] < 0:  # 합이 음수면, 커플
                R += 1
                L += 1
                result += 1
            else:  # 합이 양수면, 다음 여자
                R += 1

        else:  # 남자가 양수 일때
            if W[R] > 0: # 여자가 양수 이면, 다음 여자로
                R += 1
            elif W[R] + M[L] < 0:  #남자가 양수 여자가 음수, 커플 가능
                R += 1
                L += 1
                result += 1
            else:  # 합이 양수이면, 다음 여자
                R += 1

    print(result)

if __name__ == "__main__":
    solution()
