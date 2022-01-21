#014.우박수 구하기
A=[0 , 1]
for n in range(2,1000000):
    G = 0
    while n > len(A)-1:
        if n % 2 == 0 :  
            n /= 2
            G += 1
        else:
            n = 3* n + 1
    A.append( G + A[int(n)] )
    
print(A.index(max(A)))

