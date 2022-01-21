def start(string) :
  if string == 'EOI':
    return 
  if 'nemo' in string.lower():
    print("Found")
  else :
    print("Missing")
  return start(input())

start(input())