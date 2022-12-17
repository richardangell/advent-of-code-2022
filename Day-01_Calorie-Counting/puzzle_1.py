import sys

sys.path.append("..")
import helpers  # noqa


def load_input(file: str) -> list[str]:
    """Load the input file."""

    lines = helpers.load_input(file, remove_lines_breaks=True)

    # add empty string on end to avoid extra check below
    if lines[len(lines) - 1] != "":
        lines.append("")

    return lines


def find_max_calories_held(input: list[str]) -> int:
    """Find the maximum calories held my any of the elves."""

    max_calories = 0
    calories_counter = 0

    for input_line in input:

        if input_line == "":

            if calories_counter > max_calories:

                max_calories = calories_counter

            calories_counter = 0

        else:

            calories_counter += int(input_line)

    return max_calories


if __name__ == "__main__":

    input = load_input("input_1.txt")

    result = find_max_calories_held(input)

    print(result)
