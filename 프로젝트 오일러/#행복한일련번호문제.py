#행복한일련번호문제

def HAPPY(A): #x라는 숫자를 리스트로 바꾸고
    A_LIST=[]
    while True:
        A=str(A)
        A=",".join(A)   
        A=A.split(',')
        A=sum(list(map(lambda x: int(A[x])**2,range(len(A)))))
        if A==1: return True
        elif A_LIST.count(A)==1: return False
        else: A_LIST.append(A)
Y=int(input("입력:"))
X=list(filter(lambda x:HAPPY(x),range(Y+1)))
print("1 ~ {0} 범위의 행복 수는 {1}개 이고 총합은 {2} 입니다.".format(Y,len(X),sum(X)))