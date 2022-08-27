from collections import deque
inf = float("inf")

def solution():
    R, C = map(int, input().split())
    G = [list(input()) for i in range(R)]
    S = set()
    for r in range(R):
        for c in range(C):
            if G[r][c] == "B":
                a = (r, c)
                G[r][c] = "."
            if G[r][c] == "R":
                b = (r, c)
                G[r][c] = "."
            if G[r][c] == "O":
                hole = (r, c)
    S.add((*a, *b))
    dq = deque()
    dq.append([*a, *b, 0])
    while dq:
        r_b, c_b, r_r, c_r, times = dq.popleft()
        if times > 9:
            break
        # print(times+1)
        for rr, cc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            r_b1, c_b1, r_r1, c_r1 = r_b, c_b, r_r, c_r

            while True:
                r_b2 = r_b1 + rr
                c_b2 = c_b1 + cc
                r_r2 = r_r1 + rr
                c_r2 = c_r1 + cc

                if 0 <= r_b2 < R and 0 <= r_r2 < R \
                    and 0 <= c_b2 < C and 0 <= c_r2 < C:
                    if G[r_b2][c_b2] == "O":
                        r_b1, c_b1, r_r1, c_r1 = r_b, c_b, r_r, c_r
                        break

                    if G[r_r2][c_r2] == "O":
                        if G[r_b2][c_b2] == "#":
                            print(times+1)
                            return
                        else:
                            while True:
                                r_b2 += rr
                                c_b2 += cc
                                if G[r_b2][c_b2] == "O":
                                    break
                                elif G[r_b2][c_b2] == "#":
                                    print(times + 1)
                                    return

                    elif G[r_b2][c_b2] == "." and G[r_r2][c_r2] == ".":
                        r_b1, c_b1 = r_b2, c_b2
                        r_r1, c_r1 = r_r2, c_r2
                        continue

                    if G[r_b2][c_b2] == "#" and G[r_r2][c_r2] == "#":
                        # print("can't move")
                        break

                    if G[r_b2][c_b2] == "#": # fixed Blue
                        if r_b1 == r_r2 and c_b1 == c_r2:  # overlap
                            break
                        else:
                            r_r1, c_r1 = r_r2, c_r2
                            continue

                    if G[r_r2][c_r2] == "#": # fixed Red
                        if r_r1 == r_b2 and c_r1 == c_b2:  # overlap
                            break
                        else:
                            r_b1, c_b1 = r_b2, c_b2
                            continue

                    else:
                        break
                else:
                    break


            if (r_b1, c_b1, r_r1, c_r1) not in S:
                # print([r_b1, c_b1, r_r1, c_r1])
                S.add((r_b1, c_b1, r_r1, c_r1))
                dq.append((r_b1, c_b1, r_r1, c_r1, times + 1))


    print(-1)


if __name__ == '__main__':
    solution()
