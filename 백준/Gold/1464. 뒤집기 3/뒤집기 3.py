def solution():
    s = input()
    s1 = s[0]

    for i in range(1, len(s)):
        if s1[i-1] < s[i]:
            s1 = s[i]+s1

        else:
            s1 = s1+s[i]
    print(s1[::-1])

if __name__ == "__main__":
    solution()