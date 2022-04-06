# 자연수 N이 주어졌을 때, N의 각 자리수를 K 제곱 한후에 S(N)


# A 보다 크고
# B 보다 작거나 같고
# K 제곱


A, B, C = 1, 5, 2


graph = [0] * (B+1)
graph[1] = 0
print(graph)

def pow(X, N):
    result = 0
    text = str(X)
    for i in range(len(text)):
        result += int(text[i])**N
    return result

for i in range(A, B+1): # from A to B
    X = set()
    print("")
    print(f'start {i}')
    result = i
    while True:
        result = pow(result, C)
        # print(result)
        if result in X:
            break
        else:
            X.add(result)
    graph[i] = min(X)
    print(X)

# print(graph)
print(sum(graph))