# message = str.capitalize("first message")
# print(message)

# message = "second message".capitalize()
# print(message)

# message = "third message"
# print(message.capitalize())

# Changing case from UPPER to lower
# message = "hello world"
# print(message.lower())
# print(message.upper())

# message = message.title()
# print(message)
# print(message.swapcase())

# Count the number of characters in a string

# location = "Mississippi"
# print(location.count("s"))

# message = "racecar"
# print(message.startswith("r"))
# print(message.startswith("a"))
# print(message.startswith("ra"))

# print(message.endswith("r"))
# print(message.endswith("a"))
# print(message.endswith("ar"))

# step 6
# message = "The quick brown fox jumps over the lazy dog"
# print(message.find("q"))

# print(message.find("t"))
# print(message.find("T"))
# print(message.find("br"))

# step 7
# message = "    middle     "
# print("." + message.lstrip() + ".")
# print("." + message.rstrip() + ".")
# print("." + message.strip() + ".")

# # Step 8: Replace
# message = "brevity is the essence of wit"
# message = message.replace("essence", "soul")
# print(message)

# Step 9: Justify
message = "howdy"
message2 = "Sinothi"
print(message.rjust(20))
print(message2.rjust(20, "-"))
print(message.ljust(20))
print(message.ljust(20, "-"))
