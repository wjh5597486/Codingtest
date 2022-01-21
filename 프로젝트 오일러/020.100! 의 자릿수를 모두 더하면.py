X = 1
for i in range(1,100+1):
    X *= i
X = sum(list(map(int,str(X))))
print(X)