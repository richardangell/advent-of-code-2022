import puzzle_1


def find_sum_top_3_calories_held(input: list[str]) -> int:
    """Find the total calories held by the elves, individually holding the top
    3 amounts of calories."""

    calorie_counts = []
    calories_counter = 0

    for input_line in input:

        if input_line == "":

            calorie_counts.append(calories_counter)
            calories_counter = 0

        else:

            calories_counter += int(input_line)

    calorie_counts = sorted(calorie_counts)

    top_3_calorie_counts = calorie_counts[len(calorie_counts) - 3 :]

    return sum(top_3_calorie_counts)


if __name__ == "__main__":

    input = puzzle_1.load_input("input_1.txt")

    result = find_sum_top_3_calories_held(input)

    print(result)
