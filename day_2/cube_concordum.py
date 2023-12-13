import re


def find_game_number(string: str) -> int:
    game_number = string.split(":")[0].split(" ")[-1]
    return int(game_number)


def validate_cubes(color_list: list, color: str) -> bool:
    for value in color_list:
        if color == "red" and value > 12:
            return False
        if color == "green" and value > 13:
            return False
        if color == "blue" and value > 14:
            return False
    return True


def create_cube_list_for_color(string: str) -> list:
    color_counts_red = re.findall(f"(\d+)\s+red", string)
    color_counts_green = re.findall(f"(\d+)\s+green", string)
    color_counts_blue = re.findall(f"(\d+)\s+blue", string)
    red_list = [int(num) for num in color_counts_red]
    green_list = [int(num) for num in color_counts_green]
    blue_list = [int(num) for num in color_counts_blue]
    return red_list, green_list, blue_list


with open("day_2/puzzle_input.txt", "r", encoding="utf-8") as file:
    id_list = []
    for line in file:
        game_id = find_game_number(line.strip())
        red, green, blue = create_cube_list_for_color(line.strip())
        if validate_cubes(red, "red") and validate_cubes(green, "green") and validate_cubes(blue, "blue"):
            id_list.append(game_id)
    print(sum(id_list))
