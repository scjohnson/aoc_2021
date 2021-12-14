
goods = ['{}', '()', '[]', '<>']

scores = {'(': 1, '[': 2, '{': 3, '<': 4}


def complete_score(line):
    stack = []
    for l in line:
        if l in ')]}>':
            s = stack.pop()
        else:
            stack.append(l)
    score = 0
    stack.reverse()
    for s in stack:
        score *= 5
        score += scores[s]
    return score


def score(line):
    stack = []
    for l in line:
        if l in ')]}>':
            s = stack.pop()
            if s+l not in goods:
                if l == ')':
                    return 3
                elif l == ']':
                    return 57
                elif l == '}':
                    return 1197
                else:
                    return 25137
        else:
            stack.append(l)
    return 0


if __name__ == "__main__":
    s = 0
    s2 = []
    for ins in open("input_10.txt"):
        s_temp = score(ins)
        if s_temp == 0:
            s2.append(complete_score(ins.strip()))
        else:
            s += score(ins)
    print(s, sorted(s2)[int(len(s2)/2)])
