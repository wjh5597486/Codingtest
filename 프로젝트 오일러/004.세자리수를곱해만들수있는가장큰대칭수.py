#004.세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수.
#뒤로 읽어도 같은 수.
#세자리수 곱셈 최소값 
# 100x100 999x999                    
# 10000    998001


A=[]
for i in range(100,1000):
    for j in range(100,1000):
        A += [i*j]

A.sort(reverse=True)

for i in A:
    if str(i) == str(i)[::-1]: 
        print(i)
        break
