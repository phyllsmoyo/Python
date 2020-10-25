# Step 1 - Create a new file
# Exercise - Use the `format()` function and format strings


# Step 2 - format() function's merge feature

# medicine = "Coughussion"
# dosage = 5
# duration = 4.5

# instructions = "{} - Take {} ML by mouth every {} hours".format(
#     medicine, dosage, duration
# )
# print(instructions)

# instructions = "{2} - Take {1} ML by mouth every {0} hours".format(
#     medicine, dosage, duration
# )
# print(instructions)

# instructions = "{medicine} - Take {dosage} ML by mouth every {duration} hours".format(
#     medicine="Sneezergen", dosage=10, duration=6
# )
# print(instructions)

# Step 3 - f-strings

# name = "World"
# message = f"Hello, {name}."
# print(message)

# count = 10
# value = 3.14
# message = f"Count to {count}. Multiply by {value}"
# print(message)

# Step 4: valuate simple expressions in the replacement field of an f-string

# width = 5
# height = 10

# print(
#     f"The perimeter is {(2 * width) + (2 * height)} and the area is {width * height}."
# )

# Step 5: define format specifiers to control alignment and padding
value = "hi"

print(f".{value:<25}.")
print(f".{value:>25}.")
print(f".{value:^25}.")
print(f".{value:-^25}.")

