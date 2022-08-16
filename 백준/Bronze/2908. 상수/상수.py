def solution():
    a, b = input().split()
    a_r = ''.join(reversed(a))
    b_r = ''.join(reversed(b))

    print(a_r) if a_r > b_r else print(b_r)

if __name__ == '__main__':
    solution()