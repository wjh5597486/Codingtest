import sys
for i in sorted(list(set([sys.stdin.readline().strip() for _ in range(int(input()))])), key=lambda x: [len(x), x]):
    print(i)
