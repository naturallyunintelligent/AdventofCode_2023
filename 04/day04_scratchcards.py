from re import match

#input_text_file = "sample.txt"
input_text_file = "input.txt"

def load_data(input_text_file):
    with open(input_text_file) as input_file:
        data = []
        for index, line in enumerate(input_file):
            data.append(line.strip())
    return data

def scratch_the_card(card):
    card_contents = card.split(':')[1]

    winning_numbers = set(card_contents.split('|')[0].split())
    numbers_you_have = set(card_contents.split('|')[1].split())

    your_winning_numbers = winning_numbers & numbers_you_have

    if len(your_winning_numbers) == 0:
        score = 0
    elif len(your_winning_numbers) == 1:
        score = 1
    else:
        score = pow(2, len(your_winning_numbers)-1)
    return score

def scratch_the_cards(data) -> list[str]:
    card_points = []
    for card in data:
        card_points.append(scratch_the_card(card))
    return card_points



if __name__ == '__main__':

    data = load_data(input_text_file)

    card_points = scratch_the_cards(data)

    total_points = sum(card_points)

    if input_text_file == "sample.txt":
        assert total_points == 13

    print(f"{total_points=}")

    #store answer as a comment
    #
    #25183