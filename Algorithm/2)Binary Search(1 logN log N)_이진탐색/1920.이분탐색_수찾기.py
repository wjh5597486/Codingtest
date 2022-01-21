N = input()
NN = input()
M = input()
MM = input()

NN = list(map(int, NN.split(' ')))
NN.sort()
MM = list(map(int, MM.split(' ')))


def Binary(NN,value,left_index,right_index):

    mid_index = ( left_index + right_index ) //2 
    
    if mid_index < value:
        Binary


    if NN[right_index] == value:
        return 1
    else:
        return 0

for i in range(len(MM)):
    print( Binary(NN,MM[i],0,N))