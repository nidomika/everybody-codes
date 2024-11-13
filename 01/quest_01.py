from functions import read_input, split_list

def part1(input_data) -> int:
    return sum(0 if x == 'A' else 1 if x == 'B' else 3 for x in input_data)


def part2(input_data) -> int:
    input_data = [x.replace('x', '') for x in list(split_list(input_data, 2))]
    counter = 0
    for pair in input_data:
        counter += sum(0 if x == 'A' else 1 if x == 'B' else 3 if x == 'C' else 5 for x in pair)
        if len(pair) == 2:
            counter += 2
    return counter


def part3(input_data) -> int:
    input_data = [x.replace('x', '') for x in list(split_list(input_data, 3))]
    counter = 0
    for pair in input_data:
        counter += sum(0 if x == 'A' else 1 if x == 'B' else 3 if x == 'C' else 5 for x in pair)
        if len(pair) == 2:
            counter += 2
        elif len(pair) == 3:
            counter += 6
    return counter


input1 = read_input("01/part1.txt")
print(part1(input1))

input2 = read_input("01/part2.txt")
print(part2(input2))

input3 = read_input("01/part3.txt")
print(part3(input3))
