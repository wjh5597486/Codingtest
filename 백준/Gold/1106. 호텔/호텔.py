def solution():
    customer_goal, N = map(int, input().split())
    G = []
    for i in range(N):  # Maximum = 20
        G.append(list(map(int, input().split())))  # Cost, Customer

    graph = [float("inf")] * 1200 # Cost graph
    graph[0] = 0
    for i in range(1010):
        cur_cost = graph[i]
        for add_cost, customer in G:
            expect_cost = cur_cost + add_cost
            next_customer = i + customer
            next_cost = graph[next_customer]
            if next_cost > expect_cost:
                graph[next_customer] = expect_cost

    print(min(graph[customer_goal:]))

if __name__ == "__main__":
    solution()
