prime_lst =[2,3,5,7]
i = prime_lst[-1]+1
while len(prime_lst)<10001:
    cnt = 0
    for j in prime_lst:
        if i % j ==0:
            i+=1
            break
        else:
            cnt +=1
    if cnt == len(prime_lst):
        prime_lst.append(i)
        i += 1
print(prime_lst[-1])