from itertools import combinations
def solution():
    N, C = map(int, input().split())
    L = list(input().split())

    A = []
    for t in ['a', 'e', 'i', 'o', 'u']:
        if t in L:
            A.append(L.pop(L.index(t)))

    S = set()
    for l in range(2, N):
        consonant = list(combinations(L, l))

        vowel = list(combinations(A, N-l))

        for i in consonant:
            for j in vowel:
                S.add(''.join(sorted(i+j)))

    for i in sorted(list(S)):
        print(i)


if __name__ == '__main__':
    solution()
