def solution():
    for i in range(int(input())):
        start, end = map(int, input().split())
        rest = end - start
        speed = 0
        result = 0
        while rest > 0:
            # print(f'speed:{speed},rest:{rest}')
            for next_speed in  [speed + 1, speed, speed - 1]:
                #  감속 가능 거리
                need_rest = int((next_speed + 1) * next_speed / 2)
                if need_rest <= rest:
                    speed = next_speed
                    rest -= next_speed
                    result += 1
                    break
        # print(f'speed:{speed},rest:{rest}')
        print(result)

if __name__ == "__main__":
    solution()
