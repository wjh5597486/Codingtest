#1~20사이의 어떤수로도 나누어 떨어지는 가장 작은수.
#1~20까지의 소수의 곱으로 표현

def find():
    prime = [2,3,5,7,11,13,17,19]
    primeX = 1
    for i in prime : primeX *= i
    n=0 
    while True:
        n += primeX 
        for i in (set(range(2,21))-set(prime)) :
            if n  % i != 0: 
                break
            elif i==20 : return n

print(find())