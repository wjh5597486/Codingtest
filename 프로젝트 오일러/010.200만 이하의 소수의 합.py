#010.200만 이하의 소수의 합
### 더느려졌다......
### set 사용할 때 보다 더 느려짐.. 헐 ㅠㅠ


B = list(range(2,200+1))

for i in B :   # 3 5 7 9
    n = i 
    print(i)
    while n <= 200 and n != 0:
        print(n)
        print(B[n])
        B[n] = 0
        n += i

print(B)