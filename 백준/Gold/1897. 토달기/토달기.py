import sys
def solution():
    N, text = input().split()
    set_list = [[] for i in range(81)]
    for i in range(int(N)):
        word = sys.stdin.readline().strip()
        set_list[len(word)].append(word)

    def check(a, b):
        j = 0
        for i in range(len(a)):
            if a[i] == b[i+j]:
                continue
            if j == 0:
                j = 1
            if a[i] == b[i+j]:
                continue
            return False
        return True


    text = [text]
    S = set()
    i = 0
    while i < len(text):
        cur_word = text[i]
        i += 1
        if cur_word in S:
            continue
        S.add(cur_word)
        next_words = set_list[len(cur_word)+1]

        for next_word in next_words:
            if check(cur_word, next_word) is True:
                text.append(next_word)

    print(text[-1])



if __name__ == '__main__':
    solution()