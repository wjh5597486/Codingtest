N = int(input())

result = -1
for i in range(0,N+1,3):
    if (N-i) % 5 == 0:
        result= (i // 3) + (N - i)//5
        break
print(result)

