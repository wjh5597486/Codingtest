new_id = "...!@BaT#*..y.abcdefghijklm"

def solution(new_id) : 
  result = []
  for i in new_id:
    if i.isalnum() or i in ['.', '-', '_']:
      result +=  i.lower()
  
  for i in range(1,len(result)):
    if result[i] == result[i+1] and result[i]== '.':
      result[i] == ''
  


  print(result)
  # if len(new_id) > 15:
  #   new_id = new_id[0:14]
  
  # if new_id == '':
  #   return 'a'

  # result = []
  # for i in range(2,len(new_id-1)):
  #   if new_id[i] == new_id[i-1] == '.':
  #     result += new_id[i]

  # while len(result) < 3:
  #   result = result + result[-1] 



answer = solution(new_id)
print(answer)