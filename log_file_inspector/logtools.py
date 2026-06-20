def count_lines(filename):
    with open(filename, "r") as file:
        return len(file.readlines())

def count_words(filename):
    with open(filename, "r") as file:
        return len(file.read().split())

def count_characters(filename):
    with open(filename, "r") as file:
        return len(file.read())