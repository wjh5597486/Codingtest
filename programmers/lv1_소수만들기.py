# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다
# . 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들
# 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도
# 록 solution 함수를 완성해주세요.


def check(n):
  for i in range(2,n):
    if n % i == 0:
      return 0
  return 1

def solution(nums):
  result = 0
  leng=len(nums)
  for i in range(0,leng-2):
    for j in range(i+1,leng-1):
      for k in range(j+1,leng):
        sum = nums[i]+nums[j]+nums[k]
        if check(sum) == 1:
          print(sum)
          result += 1
  return result
          

# nums = [1,2,7,6,4]	
# print(solution(nums))
