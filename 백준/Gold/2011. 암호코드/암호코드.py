def solution():
    S = dict()
    for i in range(1, 27):
        S[str(i)] = chr(64 + i)

    string = input()

    if string[0] == '0':
        print(0)
        return

    G = [1] + [0] * (len(string) - 1) + [1]

    for i in range(1, len(string)):
        if S.get(string[i - 1:i + 1]) is None and string[i] == '0':
            print(0)
            return

        if string[i] != '0':
            G[i] += G[i - 1] % 1000000

        if S.get(string[i - 1:i + 1]) is not None:
            G[i] += G[i - 2] % 1000000

    print(G[-2] % 1000000)


if __name__ == '__main__':
    solution()
