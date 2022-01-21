N = int(input())
A, B, C = 1, 1, 1

for i in range(2, N+1):
  C =( A + B )% 15746
  A = B
  B = C
        
print(C)