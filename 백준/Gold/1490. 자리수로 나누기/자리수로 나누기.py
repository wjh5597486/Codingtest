def solution():
    import math
    string = input()
    nums = list(map(int, string))
    while 0 in nums:
        nums.remove(0)

    LCM = math.lcm(*nums)

    if int(string) % LCM == 0:
        print(string)
        return

    for j in range(1, 100): # length of the additional number.
        for i in range(10**j):
            add = str(i)
            while len(add) < j:
                add = "0" + add
            number = int(string + add)
            if number % LCM == 0:
                print(number)
                return

if __name__ == '__main__':
    solution()