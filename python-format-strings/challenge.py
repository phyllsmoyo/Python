# Step 1 - Add a new file

# Step 2

first_value = "  FIRST challenge         "
second_value = "-  second challenge  -"
third_value = "tH IR D-C HALLE NGE"

fourth_value = "fourth"
fifth_value = "fifth"
sixth_value = "sixth"

print(first_value.strip().capitalize().rjust(22))
print(second_value.strip("-").strip().capitalize())
print(third_value.replace(" ", "").replace("-", " ").capitalize().rjust(30))

print(fourth_value, fifth_value, sixth_value, sep="#", end="!")
print("\n" + fourth_value.rjust(14))
print(fifth_value.rjust(13))
print(sixth_value.rjust(13))
