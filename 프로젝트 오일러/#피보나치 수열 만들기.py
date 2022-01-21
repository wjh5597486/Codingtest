#피보나치 수열 만들기
x=12345678999
y=99987654321
B = 0
A = [0, 1]
while A[-1] <= y : 
    A.append(A.pop(0) + A[-1])
    if A[0] >= x : B += A[0] 
print(B)
