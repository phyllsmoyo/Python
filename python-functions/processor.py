def process_numbers(a):
    numbers = []
    if isinstance(a, list):
        for num in a:
            if isinstance(num, int):
                numbers.append(num)
            elif num.isnumeric():
                numbers.append(int(num))

    return sorted(numbers)


def process_names(b):
    words = []
    if isinstance(b, list):
        for word in b:
            if isinstance(word, str):
                if not word.isnumeric():
                    words.append(word)

    return sorted(words)
