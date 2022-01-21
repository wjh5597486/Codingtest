#10001번째 소수

X=2
A=[2]
while len(A)<10001:
    X=X+1                   #현재 확인하는 숫자.
    i=0
    while  True:
        if X%A[i]==0: 
            break
        else: i=i+1
        if i>len(A)-1:
            A.append(X)
            break
print(A.pop())