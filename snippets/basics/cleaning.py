# -*- coding: utf-8 -*-
# %%

def basic_open(file):
    """Open and read a file."""
    with open(file, 'r', encoding="utf=8") as f:
        f = f.readlines()

    return f


f = basic_open("file.txt")
print(f"basic_open: {f}\n")  # Get file as list of strings

# %%


def remove_space(file):
    """Remove all whitespace from file."""
    cleaned = []

    with open(file, 'r', encoding="utf=8") as f:
        for line in f:
            if not line.isspace():
                cleaned.append(line.split())
        return cleaned


f = remove_space("file.txt")
# File as a list of lists of strings, each line a new
print(f"remove_space: {f}\n")


# %%
def keep_numbers(file):
    """Get all ints in the file text."""
    cleaned = []
    with open(file, "r", encoding="utf-8") as f:
        f = f.readlines()
        for line in f:
            filtered = list(map(int, filter(lambda x: x.isnumeric(), line)))
            if len(filtered) > 0:
                strings = "".join(list(map(str, filtered)))
                cleaned.append(int(strings))
    return cleaned


f = keep_numbers("file.txt")
print(f'keep_numbers: {f}\n')  # File returns as list of ints, no whitepsace

# %%


def keep_alphanumeric(file):
    """Get all string in text file."""
    cleaned = []
    with open(file) as f:
        for line in f:
            line = line.split()
            if not len(line) == 0:
                line = list(line[0])
                line = list(map(str, filter(lambda x: x.isalpha(), line)))
                line = "".join(line)
                if not line == "":
                    cleaned.append("".join(line))
    return cleaned


f = keep_alphanumeric("file.txt")
print(f"keep_alphanumeric: {f}\n")

# %%


def remove_special_chars(file):
    pass


def replace_charactes(file):
    pass


def replace_multiple_characters(file):
    pass
def replace_multiple_characters(file):
    pass
