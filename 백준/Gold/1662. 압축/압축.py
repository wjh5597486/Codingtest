def solution():
    string = input()
    result = ""
    for idx, t in enumerate(string[0:len(string)-1]):


        if str.isnumeric(t) and str.isnumeric(string[idx+1]):
            result += "+1"

        if str.isnumeric(t) and string[idx+1] == "(":
            result += f"+{t}*("

        if str.isnumeric(t) and string[idx+1] == ")":
            result += "+1"

        if t =="(" and string[idx+1] == ")":
            result += "0"

        if t == ")":
            result += ")"


    if string[-1] == ")":

        result += ")"
    else:
        result += "+1"
    print(eval(result))



if __name__ == '__main__':
    solution()
