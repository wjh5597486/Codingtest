import re
t = input()
p = re.compile('.*nemo', re.I)
if p.fullmatch(t):
    print("Found")
else:
    print("Missing")
