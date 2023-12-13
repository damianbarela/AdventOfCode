import re


def create_cube_list_for_color(string: str) -> list:
    color_counts_red = re.findall(f"(\d+)\s+red", string)
    color_counts_green = re.findall(f"(\d+)\s+green", string)
    color_counts_blue = re.findall(f"(\d+)\s+blue", string)
    red_list = [int(num) for num in color_counts_red]
    green_list = [int(num) for num in color_counts_green]
    blue_list = [int(num) for num in color_counts_blue]
    return red_list, green_list, blue_list


with open("day_2/puzzle_input.txt", "r", encoding="utf-8") as file:
    power_list = []
    for line in file:
        red, green, blue = create_cube_list_for_color(line.strip())
        red_value = max(red)
        green_value = max(green)
        blue_value = max(blue)
        power_list.append(red_value * green_value * blue_value)
    print(sum(power_list))