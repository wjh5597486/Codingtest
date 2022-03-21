# import sys
# input = sys.stdin.readline

def check(data):
    stack = [')']
    for i in data:
        if i == "(":
            stack.append(i)
        elif stack[-1] == "(":
            stack.pop()
        else:
            return "NO"
    if len(stack) == 1:
        return "YES"
    else:
        return "NO"

N = int(input())
for __ in range(N):
    X = input()
    Y = [ X[i] for i in range(len(X))]
    print(check(Y))