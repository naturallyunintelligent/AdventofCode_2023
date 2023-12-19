import re
from functools import reduce

#input_text_file = "sample.txt"
input_text_file = "input.txt"

def load_data(input_text_file):
    with open(input_text_file) as input_file:
        data = []
        for index, line in enumerate(input_file):
            data.append(line.strip())
    return data


def assess_games(data):
    game_powers = []
    for game in data:
       game_powers.append(get_game_power(game))

    return game_powers


def get_game_power(game):
    min_cubes = [0,0,0]
    game_contents = game.split(':')[1]
    game_contents = game_contents.split(';')
    for round in game_contents:
        min_cubes = update_min_cubes(round, min_cubes)

    power = reduce(lambda x, y: x * y, min_cubes)
    return power

def update_min_cubes(round, min_cubes):
    round = round.split(',')

    for cube_sample in round:
        if "red" in cube_sample:
            sample = int(re.sub("[^0-9]", "", cube_sample))
            if min_cubes[0] < sample:
                min_cubes[0] = sample
        if "green" in cube_sample:
            sample = int(re.sub("[^0-9]", "", cube_sample))
            if min_cubes[1] < sample:
                min_cubes[1] = sample
        if "blue" in cube_sample:
            sample = int(re.sub("[^0-9]", "", cube_sample))
            if min_cubes[2] < sample:
                min_cubes[2] = sample

    return min_cubes


if __name__ == '__main__':

    data = load_data(input_text_file)

    game_powers = assess_games(data)

    sum_of_powers = sum(game_powers)

    if input_text_file == "sample.txt":
        assert sum_of_powers == 2286

    print(f"{sum_of_powers=}")

    #store answer as a comment
    #
    #65122