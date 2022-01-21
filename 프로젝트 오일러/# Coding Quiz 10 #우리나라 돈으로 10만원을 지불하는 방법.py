# Coding Quiz 10 #우리나라 돈으로 10만원을 지불하는 방법
import math
def F(X):
    X=math.factorial(X)
    return X

A=[]
B=[]
for i in range(10):
    A.append(50000**i)
    B.append((F(9)/F(9-i)/F(i)))

print(A)
print(B)
C=[]
x=100000
for i in range(10):
    C.append(A[i]*B[i]*x**(9-i))

C=sum(C)/C[9]
print(C)
#print(A)
#X=A%(10**10)