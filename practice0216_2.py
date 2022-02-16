def solution(pars):
    answer = [0] * len(pars)
    stack = []

    for index in range(len(pars)):
        stack = []
        if len(pars[index]) % 2 != 0:
            answer[index] = 0
            continue

        for char in pars[index]:
            if char in ['[', '{', '(']:
                stack.append(char)
            else:
                x = stack.pop()
                if pair_validation(stack, x, char) == 0:
                    answer[index] = 0
                    break
                else:
                    answer[index] = 1
    return answer


def pair_validation(arr, n, k):
    check = 1
    if '(' in arr and k in [']', '}']:
        check = 0
    elif '{' in arr and k == ']':
        check = 0
    else:
        if (n == '[' and k == ']') or (n == '{' and k == '}') or (n == '(' and k == ')'):
            check = 1
        else:
            check = 0
    return check


pars = ['[(){{()}}]', '([])', '[()]()[{}]', '(}', '()', '{}', '[]']

print(solution(pars))
