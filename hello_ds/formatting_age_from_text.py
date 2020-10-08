# Formatting the age
def format_age(r):
    chars = list(r)  # list of characters
    digit_chars = [c for c in chars if c.isdigit()]
    return int("".join(digit_chars))


a = "I am 25 years old"

print(format_age(a))
