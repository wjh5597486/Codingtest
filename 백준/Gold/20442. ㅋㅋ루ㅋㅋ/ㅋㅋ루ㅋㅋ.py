def solution():

    G = input()
    acc = 0
    b = 0
    LK = []
    R = []
    for i in G:
        if i =="K":
            acc += 1
            b = 0
        else:
            b += 1
            R.append(b)
            LK.append(acc)

    acc = 0
    RK = []
    for i in G[::-1]:
        if i =="K":
            acc += 1
        else:
            RK.append(acc)
    RK.reverse()

    result = 0

    l, r = 0, len(R)-1
    while l <= r:
        result = max(result, r-l+1 + 2*min(LK[l], RK[r]))

        if LK[l] < RK[r]:
            l += 1
        else:
            r -= 1
    print(result)


if __name__ == "__main__":
    solution()

