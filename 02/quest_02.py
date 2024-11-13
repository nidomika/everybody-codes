import re
from functions import read_input


def part1(input_data: str) -> int:
    counter = 0
    for word in input_data[0].split(','):
        counter += input_data[1].count(word)

    return counter


def part2(input_data: str) -> int:
    counter = 0
    for sentence in input_data[2:]:
        found_indexes = []
        for word in input_data[0].split(','):
            reversed_sentence = sentence[::-1]
            for match in re.finditer(word, sentence):
                for index in range(match.start(), match.end()):
                    found_indexes.append(index)
            for match in re.finditer(word, reversed_sentence):
                for index in range(match.start(), match.end()):
                    found_indexes.append(len(sentence) - index - 1)
    counter += len(set(found_indexes))

    return counter


def part3(input_data: str) -> int:
    counter = 0
    for sentence in input_data[2:]:
        found_indexes = []
        for word in input_data[0].split(','):
            reversed_sentence = sentence[::-1]
            for match in re.finditer(word, sentence):
                for index in range(match.start(), match.end()):
                    found_indexes.append(index)
            for match in re.finditer(word, reversed_sentence):
                for index in range(match.start(), match.end()):
                    found_indexes.append(len(sentence) - index - 1)
    counter += len(set(found_indexes))

  # rotate list input_data[2:] by 90 degrees
    print(input_data[2:])
    rotated = list(zip(*input_data[2:]))
    print(rotated)

    return counter

input1 = read_input("02/part1.txt")
# print(part1())
input2 = read_input("02/part2.txt")
# print(part2())
input3 = read_input("02/part3.txt")
#print(part3())