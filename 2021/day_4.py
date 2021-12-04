
def get_input(day):
    lines = (x for x in day.input if x.strip())
    seq = (int(x) for x in next(lines).split(','))

    boards = []
    dict_ = {}
    for idx, i in enumerate(lines):
        dict_.update({int(y): (idx % 5, yidx) for yidx, y in enumerate(i.split())})

        if (idx + 1) % 5 == 0:
            boards.append((dict_.copy(), ([0] * 5, [0] * 5)))
            dict_ = {}

    return seq, boards

def sort_winners(seq, boards):
    queue = []
    found = set()

    for i in seq:
        for idx, (board, (sums_x, sums_y)) in enumerate(boards):
            if idx not in found and ((pos := board.pop(i, None)) is not None):
                x, y = pos
                sums_x[x] += 1
                sums_y[y] += 1

                if sums_x[x] >= 5 or sums_y[y] >= 5:
                    queue.append(sum(board.keys()) * i)
                    found.add(idx)

    return queue


def puzzle_1(day, *args, **kwargs):
    return sort_winners(*get_input(day))[0]

def puzzle_2(day, *args, **kwargs):
    return sort_winners(*get_input(day))[-1]

def puzzle_3(day, *args, **kwargs):
    """
    Optimizations for puzzle 1 after having looked at other peoples solutions
    """

def puzzle_4(day, *args, **kwargs):
    """
    Optimizations for puzzle 2 after having looked at other peoples solutions
    """