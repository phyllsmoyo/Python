# Getting first name and last name
def get_first_last_name(s):
    INVALID_NAME_PARTS = ["mr", "ms", "mrs", "dr", "jr", "sir"]
    parts = s.lower().replace(".", "").strip().split()
    parts = [p for p in parts if p not in INVALID_NAME_PARTS]
    if len(parts) == 0:
        raise ValueError("Name %s is formatted wrong" % s)

    first, last = parts[0], parts[-1]
    first = first[0].upper() + first[1:]
    last = last[0].upper() + last[1:]
    return first, last


s = "Mr. Donald Trump"
a = get_first_last_name(s)

print(a)
