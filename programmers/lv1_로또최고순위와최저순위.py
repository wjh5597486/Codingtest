
def solution(lottos, win_nums):
  min, max, rank = 0, 0, [6, 6, 5, 4, 3, 2, 1]
  for i in (range(6)):
    if lottos[i] == 0:
      max += 1
    elif lottos[i] in win_nums:
      min += 1
  return [ rank[min + max], rank[min]] 



lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
A = solution(lottos, win_nums)
print(A)