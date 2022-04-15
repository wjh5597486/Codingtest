def solution():
    n, P = map(int, input().split())
    G = list(map(int, input().split()))
   
    result = 100000
    left = 0
    right = 0
    sum = G[0]

    while right < n:
        if sum >= P:
            result = min(result, right-left+1)
            
            sum -= G[left]
            left += 1
            continue
        else:
            right +=1
            if right == n:
                break
            sum = sum + G[right]

    if result ==100000:
        return 0
    else:
        return result



if __name__ == '__main__':
    #solution()
    print(solution())
