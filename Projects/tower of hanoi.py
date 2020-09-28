# Code for solving the tower of Hanoi

# Let's say we have n
# we want to move them from A to C, assumig we have 3 poles A, B, C
# How many moves does it take?

# We will use python recursion


def hanoi(n, start, end, spare):

    if n == 1:
        # Move the last disk from start to the end
        print("Move from", start, "to", end)

    elif n > 0:
        # Move n-1 disks to the spare so that we can move the last disk to the end.
        # We will use the END as the spare
        hanoi(n - 1, start, spare, end)
        print("Move from", start, "to", end)
        # move n-1 disks from the SPARE to the END using the START as the spare.
        hanoi(n - 1, spare, end, start)

    else:
        return "Try again with a positive n"


n = 2
print(hanoi(n, "A", "B", "C"))