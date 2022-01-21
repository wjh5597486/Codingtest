#009. a+b+c= 1000이되는 피타고라스수
def FIND():
    for i in range(1,1000): 
        for j in range(1,997):
            if i**2+j**2==(1000-i-j)**2:
                return i*j*(1000-i-j)
print(FIND())