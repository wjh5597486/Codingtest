#012. 500개 이상의 약수를 갖는 가장 작은 삼각수는?
# 뫃르겠수당..

x, i =0 , 0 
L = 1
while True:   
    i += 1
    x += i   # 삼각수.
    
    L = 2  # 약수의 개수
    y = 2
    while True :
        if x % y == 0 : 
            L += 1 
        elif y > round(y/2):
            L += 1
            break
        y += 1
        
    print("{0}  {1}".format(x, L)) 

    if L >= 500 : break
    else : L = 1 