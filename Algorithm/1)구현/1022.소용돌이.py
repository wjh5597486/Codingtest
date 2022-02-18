n = 1
w, h = 0, 0

right = 1
up = -1
i = 0

r1, c1, r2, c2 = -1, -2, -1, 1
f = 5000

graph = [ [0] * (f*2+1) for __ in range(f*2+1)]


def check(w, h):
    if r1 <= h <= r2 and c1 <= w <= c2:
        graph[h+f][w+f] = n

check(0,0)

while True:
    i += 1
    for __ in range(i):
        n += 1
        w += right
        check(w, h)
    right *= -1

    for __ in range(i):
        n += 1
        h += up
        check(w,h)
    up *= -1

    if n >= 100020001:
        break
# for i in graph: print(i)

for i in graph[r1+f:r2+1+f]:
    print(i[c1+f:c2+f+1])