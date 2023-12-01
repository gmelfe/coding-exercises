"""Implementation for Advent of Code 2023 - day 1 exercise"""


def parse_spelling(line: str) -> str:
    spelling_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    output = ""
    i = 0
    while i < len(line):
        matches = False
        for index, number in enumerate(spelling_digits):
            if line[i:].startswith(number):
                output += str(index)
                i += len(number) - 1
                # the -1 is to account for overlapping letter
                matches = True
                break
        if not matches:
            output += line[i]
            i += 1
    return output


def sum_digits(line: str) -> int:
    digits = [char for char in line if char.isdigit()]
    return int(digits[0] + digits[-1])


def solve_part1(lines):
    acc = 0
    for line in lines:
        acc = acc + sum_digits(line)
    return acc


def solve_part2(lines):
    acc = 0
    for line in lines:
        line = parse_spelling(line)
        acc = acc + sum_digits(line)
    return acc


if __name__ == "__main__":
    with open("day01.in", "r", encoding="utf8") as input_file:
        input_lines = input_file.readlines()

        solution_1 = solve_part1(input_lines)
        print(f"Part One: {solution_1}")

        solution_2 = solve_part2(input_lines)
        print(f"Part two: {solution_2}")
