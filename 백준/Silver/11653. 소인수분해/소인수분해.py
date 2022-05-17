def solution():
    X = int(input())
    n = 2
    while n <= X:
        if X % n == 0:
            X = X / n
            print(n)
        else:
            n += 1





if __name__ == "__main__":
    solution()
