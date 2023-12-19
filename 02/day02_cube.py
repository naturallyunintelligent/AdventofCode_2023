import re

bag_contents = [12, 13, 14]

#input_text_file = "sample.txt"
input_text_file = "input.txt"

def load_data(input_text_file):
    with open(input_text_file) as input_file:
        data = []
        for index, line in enumerate(input_file):
            data.append(line.strip())
    return data


def assess_games(data, bag_contents):
    game_ids_possible = []
    for game in data:
       if check_game(game, bag_contents) is True:
           game_id = game.split(':')[0]
           game_ids_possible.append(int(re.sub("[^0-9]", "",game_id)))

    return game_ids_possible


def check_game(game, bag_contents):
    game_result = True
    game_contents = game.split(':')[1]
    game_contents = game_contents.split(';')
    for round in game_contents:
        if check_round(round, bag_contents) is False:
            game_result = False

    return game_result

def check_round(round, bag_contents):
    round = round.split(',')
    try:
        for cube_sample in round:
            if "red" in cube_sample:
                sample = int(re.sub("[^0-9]", "", cube_sample))
                if sample > bag_contents[0]:
                    return False
            if "green" in cube_sample:
                sample = int(re.sub("[^0-9]", "", cube_sample))
                if sample > bag_contents[1]:
                    return False
            if "blue" in cube_sample:
                sample = int(re.sub("[^0-9]", "", cube_sample))
                if sample > bag_contents[2]:
                    return False
    except:
        return True


if __name__ == '__main__':

    data = load_data(input_text_file)

    games_ids_possible = assess_games(data, bag_contents)

    possible_games_id_total = sum(games_ids_possible)

    if input_text_file == "sample.txt":
        assert possible_games_id_total == 8

    print(f"{possible_games_id_total=}")

    #store answer as a comment
    #
    #2879