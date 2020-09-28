# Code for solving the tower of Hanoi


def hanoi(n, start, end, via):
    if n == 1:
        print("Move from", start, "to", end)

    else:
        hanoi(n - 1, start, via, end)
        print("Move from", start, "to", end)
        hanoi(n - 1, via, end, start)


n = 1
hanoi(n, "A", "B", "C")