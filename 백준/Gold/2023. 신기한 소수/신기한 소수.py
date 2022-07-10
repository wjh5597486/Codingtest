def solution():
    import math

    def isprime(n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    N = int(input())
    result = [2,3,5,7]
    for i in range(1,N):
        new_list=[]

        for i in result:
            for num in range(1,10,2):
                new_num = i * 10 + num
                if isprime(new_num):
                    new_list.append(new_num)
        result = new_list
    result.sort()
    for i in result:
        print(i)




if __name__ == '__main__':
    solution()
