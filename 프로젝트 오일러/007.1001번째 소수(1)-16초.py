#10001번째 소수


def Check(X,A):  # X가 소수인지 확인
    i=0
    while  i<len(A):   
        if X%A[i]==0: return A
        else: i=i+1
    return A.append(X)

X=2
A=[2]
while len(A)<10001:
    X=X+1
    Check(X,A)
    

print(A.pop())