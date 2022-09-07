s = input()
r = s[0]

for t in s[1::]:

    if r[0] < t:
        r = r + t

    else:
        r = t + r
print(r)