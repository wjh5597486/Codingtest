def change(MONEY):
    MONEY=' '.join(MONEY).split(' ')
    for i in range(16-len(MONEY)) : MONEY.insert(0,'0')
    
    #convert 숫자 to 한글
    unit=','.join('영일이삼사오육칠팔구').split(',') 
    MONEY=list(map(lambda x:unit[int(MONEY[x])],range(len(MONEY))))

    unit=['천','백','십',['조','억','만',' ']]#            unit[i]
    for j in range(0,4): # 0조 1억 2만 3원  4자리씩 끊어서
        if MONEY[0:4]==['영','영','영','영']: MONEY=MONEY[4:]
        elif j==2 and MONEY[0:4]==['영','영','영','일']: MONEY=MONEY[4:]+['만',' ']
        else:            
            for i in range(4):
                if i in range(3):                   #천백십 단위일경우
                    if MONEY[0] in '영':
                        MONEY.pop(0)
                    elif MONEY[0] =='일':
                        MONEY.pop(0)
                        MONEY.append(unit[i])
                    else:
                        MONEY.append(MONEY.pop(0))
                        MONEY.append(unit[i])
                else:                               #일단위 경우.  
                    if MONEY[0] in '영': MONEY.pop(0)
                    else : MONEY.append(MONEY.pop(0))
                    MONEY.append(unit[i][j])
                    if j!=3: MONEY.append(' ')

    MONEY.pop()
    MONEY.append('원')
    print(''.join(MONEY))
    return MONEY

drawlist='''
1원
4원
8원
9원
10원
17원
79원
80원
95원
205원
809원
851원
878원
2,000원
2,800원
7,008원
8,174원
9,718원
45,150원
50,000원
69,700원
382,915원
431,409원
921,500원
5,003,052원
5,039,670원
6,835,623원
8,000,000원
10,000,003원
35,100,000원
39,997,777원
90,021,015원
93,275,690원
403,197,000원
459,176,461원
730,080,000원
999,999,000원
6,887,000,000원
7,000,020,000원
7,700,000,500원
7,848,761,270원
38,048,620,625원
57,000,000,000원
74,778,562,249원
97,417,165,814원
101,000,120,000원
343,000,000,000원
458,807,907,862원
872,818,015,000원
6,278,000,015,000원
7,991,000,844,000원
9,000,400,000,675원
22,018,914,675,100원
78,196,000,000,000원
85,000,904,224,858원
95,000,000,404,918원

'''
A=[]
drawlist=drawlist.replace('\n','').replace(',','').rstrip('원').split('원') #리스트 배열
#print(drawlist)

A=list(map(lambda x:change(x),drawlist)) #리스트 순서대로 처리
A=list(map(lambda x:(len(A[x])-A[x].count(" "))*(A[x].count(" ")+1),range(len(A))))
print(sum(A))