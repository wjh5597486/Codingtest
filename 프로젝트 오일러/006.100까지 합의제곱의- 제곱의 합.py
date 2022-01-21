#1부터 100까지 "제곱의 합"과 "합의 제곱"의 차

A=sum(range(1,101))**2-sum(list(map(lambda x:x**2,range(1,101))))
print(A)