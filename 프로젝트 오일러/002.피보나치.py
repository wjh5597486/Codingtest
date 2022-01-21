#print(sum(filter(lambda x:x%3==0 or x%5==0 ,range(1,1000))))
#filter (범위내 조건,리스트순서대로)
#lambda (변수 : 조건식에 맞으면리턴)


A=[0,1,1]
while A[1]<4000001:
    if A[1]%2==0:A[0]=A[0]+A[1]
    A.append(A[2]+A.pop(1))
print(A[0])