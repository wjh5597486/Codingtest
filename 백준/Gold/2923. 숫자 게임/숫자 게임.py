def solution():
    import sys
    LEFT = [0]*101
    RIGHT = [0]*101
    for i in range(int(input())):
        a, b = map(int, sys.stdin.readline().split())
        LEFT[a] += 1
        RIGHT[b] += 1

        l = 0
        r = 100
        result = 0
        left = LEFT.copy()
        right = RIGHT.copy()

        while l <= 100 and r >= 0:
            if left[l] == 0:
                l += 1
                continue
            if right[r] == 0:
                r -= 1
                continue

            result = max(result, l+r)
            min_value = min(left[l], right[r])
            left[l] -= min_value
            right[r] -= min_value

        print(result)



if __name__ == '__main__':
    solution()