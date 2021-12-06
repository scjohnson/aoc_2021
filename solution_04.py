import numpy as np


def parse(input_file):
    with open(input_file) as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]
        numbers = [int(i) for i in lines[0].split(',')]
        lines = lines[1:]
        boards = []
        for i in range(int(len(lines)/6)):
            s = [" ".join(lines[i*6+1:i*6+6])]
            boards.append(np.fromstring(
                s[0], sep=' ', dtype=int).reshape([5, 5]))
        return numbers, boards


def call_number(number, boards):
    for board in boards:
        board[board == number] = 0
    return boards


def solution(input_file):
    numbers, boards = parse(input_file)
    part1 = False

    for number in numbers:
        boards = call_number(number, boards)
        new_boards = []
        for board in boards:
            if np.isin(0, np.sum(board, axis=0)) or np.isin(0, np.sum(board, axis=1)):
                if part1 == False:
                    part1 = np.sum(board)*number
                if len(boards) == 1:
                    part2 = np.sum(board)*number
                    return (part1, part2)
            else:
                new_boards.append(board)

        boards = new_boards


if __name__ == "__main__":
    print("test solution: ", solution("test_04.txt"))
    print("solution: ", solution("input_04.txt"))
