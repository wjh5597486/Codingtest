def Point(p,screen):
    p=list(map(int,p))
    p=[min(p[0],p[2]), min(p[1],p[3]) ,abs(p[0]-p[2]) ,abs(p[1]-p[3]) ]
    for x in range(p[0],p[0]+p[2]):
        for y in range(p[1],p[1]+p[3]):
            screen[x][y]=1
    return screen

coor='''1 2 3 4''' ##좌표넣는곳
screen=[[0]*1080 for i in range(1920)] #초기값
coor=list(filter(lambda x:x!='',coor.split('\n'))) #리스트 불러오기
coor=list(map(lambda i:coor[i].split(' '),range(len(coor))))

for i in range(len(coor)): Point(coor[i],screen)
screen=sum(list(map(lambda x: sum(screen[x]),range(len(screen))))) #최종 계산
print(screen)