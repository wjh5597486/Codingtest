def solution():
    num_member, K, num_dish = map(int, input().split())
    capacity = [[0] + [K] * 200 + [0] * 101] + [[0] * 302 for i in range(301)]

    dish_capacity = list(map(int, input().split()))

    for dish_num, dish_capacity in enumerate(dish_capacity):
        dish_num += 201
        capacity[dish_num][301] = dish_capacity



    flow = [[0] * 302 for _ in range(302)]

    for mem_idx in range(1, num_member+1):
        q = list(map(lambda x: int(x)+200, input().split()))[1::]
        for dish_idx in q:
            capacity[mem_idx][dish_idx] = 1


    def dfs(start, end):
        q = [start]
        check[start] = start
        while q:
            prior = q.pop()

            if prior == end:
                return True

            for posterior, cap in enumerate(capacity[prior]):
                if check[posterior] == -1:
                    if cap - flow[prior][posterior] > 0:
                        check[posterior] = prior
                        q.append(posterior)
        return False

    def update(start, end):
        posterior = end
        while posterior != start:
            prior = check[posterior]
            flow[prior][posterior] += 1
            flow[posterior][prior] -= 1
            posterior = prior

    cnt = 0
    while True:
        check = [-1] * 400
        if dfs(0, 301):
            update(0, 301)
            cnt += 1
        else:
            break

    print(cnt)


if __name__ == '__main__':
    solution()
