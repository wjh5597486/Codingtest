import sys


def solution():
    def get_divisor(n):
        n = int(n)
        divisors = []
        divisors_back = []

        for i in range(1, int(n ** (1 / 2)) + 1):
            if (n % i == 0):
                divisors.append(i)
                if (i != (n // i)):
                    divisors_back.append(n // i)

        return divisors + divisors_back

    G = [0] * 1_000_100
    member = []
    for i in range(int(input())):
        N = int(sys.stdin.readline())
        G[N] += 1
        member.append(N)

    N = 0
    for i in member:
        divisor = get_divisor(i)
        result = sum(G[j] for j in divisor) - 1
        print(result)


if __name__ == "__main__":
    solution()
