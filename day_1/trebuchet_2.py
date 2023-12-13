from __future__ import annotations

def find_first_digit_in_string(string: str, return_as_digit=True) -> str:
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    spelled_digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for _ in range(len(string)):
        for digit, spelled_digit in zip(digits, spelled_digits):
            if string.startswith(digit):
                return digit
            if string.startswith(spelled_digit):
                return spelled_digits[spelled_digit] if return_as_digit else spelled_digit
        string = string[1:]


def find_last_digit_in_string(string: str) -> str:
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    spelled_digits = {"eno": "1", "owt": "2", "eerht": "3", "ruof": "4", "evif": "5", "xis": "6", "neves": "7", "thgie": "8", "enin": "9"}
    # first_digit = find_first_digit_in_string(string, return_as_digit=False)
    # string = string.replace(first_digit, "", 1)
    string = string[::-1]
    for _ in range(len(string)):
        for digit, spelled_digit in zip(digits, spelled_digits):
            if string.startswith(digit):
                return digit
            if string.startswith(spelled_digit):
                return spelled_digits[spelled_digit]
        string = string[1:]


def calculate_calibration_value(first_digit: str | None, last_digit: str | None):
    if first_digit and last_digit:
        return int(first_digit + last_digit)
    if first_digit:
        return int(first_digit)
    return int(last_digit)


def main():
    calibration_value_list = []
    with open("day_1/puzzle_input.txt", "r", encoding="utf-8") as file:
        for line in file:
            first_digit = find_first_digit_in_string(line.strip())
            last_digit = find_last_digit_in_string(line.strip())
            calibration_value = calculate_calibration_value(first_digit, last_digit)
            calibration_value_list.append(calibration_value)
            print(first_digit, last_digit)
    answer = sum(calibration_value_list)
    print(answer)


if __name__ == "__main__":
    main()
