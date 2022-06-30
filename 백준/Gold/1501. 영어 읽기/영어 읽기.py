from functools import reduce
# 사전의 입력이 중복되는 경우가 인가? No.
# 사전 입력에서 입력이 중복되는 경우가 인가? No.
# 75% 실패
# 한 글자 처리 오류 수정.
# 긴 문장에서 일부 단어가 불가능하더라도 0이 안나오는 이게 맞나????

def solution():
    graph = dict()
    S = set()
    for i in range(int(input())):
        string = input()
        if string in S:
            continue
        else:
            S.add(string)
        if len(string) == 1:
            graph[string] = 1

        else:
            string = string[0] + ''.join(sorted(list(string[1:-1]))) + string[-1]
            graph[string] = 1 if graph.get(string) is None else graph[string] + 1

    for i in range(int(input())):
        line = list(input().split())
        result = []
        if len(line) == 1:
            string = line[0]
            string = string[0] + ''.join(sorted(list(string[1:-1]))) + string[-1]
            if len(line[0]) == 1:
                string = line[0]
            result.append(0 if graph.get(string) is None else graph[string])
        else:
            for string in line:
                string = string[0] + ''.join(sorted(list(string[1:-1]))) + string[-1]
                number = 1 if graph.get(string) is None else graph[string]
                result.append(number)

        X = reduce(lambda x,y: x*y, result)
        print(X)

if __name__ == "__main__":
    solution()