def solution():
    N = int(input())
    P = set()
    P.add(tuple(list(map(int, input().split()))))
    S = list(map(int, input().split()))

    record = set()

    card = [0,1,2] * int(N//3)
    for i in range(0, 1_000_000):

        if tuple(card) in P:  # correct
            print(i)
            return

        if tuple(card) in record:  # -1 end
            print(-1)
            return

        else:
            record.add(tuple(card))

        card = [card[idx] for idx in S]

if __name__ == "__main__":
    solution()