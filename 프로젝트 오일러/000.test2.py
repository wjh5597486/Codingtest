N = input()
NN = input()
M = input()
MM = input()

N=int(N)
NN = list(set(map(int, NN.split(' '))))1
NN.sort()
M=int(M)
MM = list(map(int, MM.split(' ')))


def Binary(NN, value, left_index, right_index):
    if left_index > right_index : return 0

    mid_index = ( left_index + right_index ) //2 

    if value < NN[mid_index]:
        return Binary(NN, value, left_index, mid_index-1 )

    if value > NN[mid_index]:
        return Binary(NN, value, mid_index + 1, right_index)
    
    return 1

for i in range(len(MM)):
    print( Binary(NN ,MM[i] ,0 ,len(NN)-1))