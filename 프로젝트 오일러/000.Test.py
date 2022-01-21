M = input()
N2 = input()
M = input()
M2 = input()

N2 = list(set(map(int, N2.split(' '))))
M2 = list(map(int, M2.split(' ')))
checklist = list(range(len(M2)))
checklist2 = checklist[:]

for j in checklist:
    if  0 >= M2[j]:
        M2[j] = False
        checklist2.remove(j)

checklist = checklist2[:]




for i in N2:
    checklist2=checklist[:]
    for j in checklist2:
        if i == M2[j]:
            M2[j] = True
            checklist.remove(j)



for i in M2:
    if i == True: print(1)
    else: print(0)