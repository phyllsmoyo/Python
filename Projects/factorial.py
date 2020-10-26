# calculating factorial of a number
# 0! = 1
# 1! = 1
# 2! = 2 * 1
# n! = n * (n-1) * (n-2) * ... * 1

# using recurssion i python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 1:
        return "Try again, function only takes postive integers"
    else:
        # n * (factorial of n-1)
        return n * (factorial(n - 1))


n = 50
print(factorial(n))
