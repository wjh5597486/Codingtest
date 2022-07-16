from collections import deque
def solution():
    def case():
        commend = list(input())
        input()
        A = deque(eval(input()))
        w = 1
        for c in commend:
            if c == 'R':
                w *= -1
            elif c == 'D':
                if A:
                    if w == 1:
                        A.popleft()
                    else:
                        A.pop()
                else:
                    print("error")
                    return

        A = list(A)[::w]
        if A == []:
            print("[]")
            return
        string = "["
        for i in A:
            string += str(i) + ','
        string = string[:-1]
        string += "]"
        print(string)


    for i in range(int(input())):
        case()


if __name__ == '__main__':
    solution()
