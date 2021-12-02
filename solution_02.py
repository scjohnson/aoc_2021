def process2(instruction, pos, depth, aim):
    value = int(instruction.split()[1])
    if 'down' in instruction:
        aim += value
    elif 'up' in instruction:
        aim -= value
    else:
        pos += value
        depth += aim*value
    return (pos, depth, aim)


def process(instruction, pos, depth):
    value = int(instruction.split()[1])
    if 'forward' in instruction:
        pos += value
    elif 'down' in instruction:
        depth += value
    else:
        depth -= value
    return (pos, depth)


if __name__ == "__main__":

    instruction = [i for i in open("input_02.txt")]
    pos, depth = 0, 0
    for ins in instruction:
        pos, depth = process(ins, pos, depth)
    print(pos*depth)  # 2027977

    pos, depth, aim = 0, 0, 0
    for ins in instruction:
        pos, depth, aim = process2(ins, pos, depth, aim)
    print(pos*depth)  # 1903644897
