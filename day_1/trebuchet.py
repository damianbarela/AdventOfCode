def find_first_digit_in_string(string: str) -> str:
    for letter in string:
        if letter in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return letter


def find_last_digit_in_string(string: str) -> str:
    for letter in string[::-1]:
        if letter in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return letter


def main():
    calibration_value_list = []
    with open("day_1/puzzle_input.txt", "r", encoding="utf-8") as file:
        for line in file:
            first_digit = find_first_digit_in_string(line.strip())
            last_digit = find_last_digit_in_string(line.strip())
            calibration_value = int(first_digit + last_digit)
            calibration_value_list.append(calibration_value)
    answer = sum(calibration_value_list)
    print(answer)


if __name__ == "__main__":
    main()
