def solution():
    N, M = map(int, input().split())
    input_word = input()
    string = input()

    word = dict()

    for i in range(65, 123):
        word[chr(i)] = 0

    window  = word.copy()

    for i in input_word:
        word[i] += 1

    for i in string[:len(input_word)]:
        window[i] += 1

    result = 1 if word == window else 0
    for idx, i  in enumerate(range(len(input_word), len(string))):
        window[string[idx]] -= 1
        window[string[i]] += 1
        result += 1 if word == window else 0

    print(result)

if __name__ == '__main__':
    solution()
