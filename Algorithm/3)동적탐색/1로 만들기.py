N = int(input())
result = [0, 0]
i = int(2);
while i <= N :
  result.append(result[i-1] + 1);
  if i % 2 == 0:
    result[i] = min(result[int(i/2)] + 1 ,result[i] )
  elif i % 3 == 0:
    result[i] = min(result[int(i/3)] + 1 ,result[i] )
  i += 1
print(result)


# N = 10;
# [0 1 2 3 4 5 6 ]
# [0 1 1 2 3 2 3 ] 131