#숫자 리스트로 합계가 최소인 자연수 만들기
#0이 맨앞에 오는 경우는 제외 
def make():
    A=[0, 0, 1, 8, 2, 2, 8, 9, 0, 3, 4, 0, 0]
    A.sort()
    i= A.count(0)
    if len(A) < i+2 :return -1  #자연수가 안될시 -1반환
    A= A[i:i+2] +[0]*i+ A[i+2:]
    count=0
    i=1    
    while len(A) > 2:
        count+=(A.pop()+A.pop())*i
        i*=10
    count+=sum(A)*i
    return count

print(make())