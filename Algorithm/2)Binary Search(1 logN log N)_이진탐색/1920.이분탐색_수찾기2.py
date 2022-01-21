#이분 탐색 #mid #+1-1-1

# #1)리스트는 정렬되어있어야한다. 순서가 있는 값만 가능하다.(수치화된 값)
# left right : 왼쪽 오른쪽 끝의 index값
# 범위 안의값인지 굳이 확인할 필요가 없는 이유는 일단 시도 횟수가 N 으로 적은편 (리스트:2**N) 최초의 1번 실행 이외에는 안하는게 낫다. 
# 최초 실행을 넣으면 코드가 더러워진다.
# 
def Binary(control, value, left, right):

    if left > right: return False
    
    mid = ( left + right ) // 2

    if control[mid] == value : 
        return True

    elif control[mid] < value:
        return Binary(control, value, mid +1, right)
    
    elif control[mid] > value:
        return Binary(control, value, left, mid-1)






control = list(range(0,2**22))
compare = list(range(-1,2))
for value in compare:
    print(value)
    print(Binary(control, value, 0, len(control)-1)) #control group,value,left,right ## -1 이 매우 중요하다.