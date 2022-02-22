N, S = map(int, input().split())
graph = list(map(int, input().split()))


def find(N, X):
    F = N % X
    if F == 0:
        return X
    else:
        return find(X, F)


Y = abs(graph.pop() - S)
while graph:
    X = abs(graph.pop() - S)
    if Y > X:
        Y = find(Y, X)
    else:
        Y = find(X, Y)
print(Y)


