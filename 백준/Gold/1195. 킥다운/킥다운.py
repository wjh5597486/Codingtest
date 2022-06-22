def solution():
    A = input()
    B = input()
    result = 10000

    for num in range(len(B)+1):
        a = str(0)*num + A
        for i, j in zip(a, B):
            if i == j == "2":
                break
        else:
            result = min(result, max(len(a), len(B)))

    for num in range(len(A)+1):
        b = str(0)*num + B
        for i, j in zip(A, b):
            if i == j == "2":
                break
        else:
            result = min(result, max(len(b), len(A)))

    print(result)



if __name__ == "__main__":
    solution()
