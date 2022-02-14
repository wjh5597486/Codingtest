

w = 10000
h, H, W = w, w, w
n = w * h
# left up right down
left = 1
up = 1
w += 1

r1, c1, r2, c2 = -2, -1, -1, 1
# list=[[0]* w for i in range(w)]

# 범위 안에 있는지 확인
def check():
    global list, n
    n -= 1

# w번 왼쪽으로, h-=1
def goLeft():
    global left, W, H, n, w, h

    for i in range(W):
        w = w - left
        check()
        # print(n+1, " 좌우 :  ", h, w)  # 현재 위치 확인.

    H -= 1
    left *= -1

    if n != 1:
        goUp()


# h번 위쪽으로, w-=1
def goUp():
    global up, W, H, n, w, h

    for i in range(H):
        h = h - up
        check()
        # print(n+1, " 상하 :  ", h, w)  # 현재 위치 확인.

    W -= 1

    up *= -1

    if n != 1:
        goLeft()


goLeft()
print(n, h, w-1)