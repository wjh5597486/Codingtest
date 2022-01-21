# 모든 3의 배수 +  모든 5의 배수 (1000이하)
# 리스트에 n의 배수 1000까지 반복 n=3
# 리스트 합계 더하기 


A=0
for i in range(1,1000):
    if i%3 == 0 or i%5 == 0:
        A = A + i
print(A)



A=sum(list(filter(lambda x:x%3==0 or x%5==0 ,range(1,1000))))
print(A)