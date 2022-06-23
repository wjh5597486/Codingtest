def solution():
    W, H, f, c, x1, y1, x2, y2 = map(int, input().split())

    x1 += f
    x2 += f
    height = y2 - y1
    c += 1

    if f*2 <= W: # right is wider.
        double = max(0, 2*f-x1) if 2*f <= x2 else x2-x1
        single = max(0, x2-2*f) if x1 < 2*f else x2-x1
        result = (double*2 + single) * height * c

    else:
        double = max(0, W-x1) if W <= x2 else x2-x1
        single = max(0, x2-W) if x1 < W else x2-x1
        result = (double*2 + single) * height * c
    print(W*H-result)
    
if __name__ == "__main__":
    solution()
