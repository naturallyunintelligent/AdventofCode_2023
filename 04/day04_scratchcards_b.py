from re import match

#input_text_file = "sample.txt"
input_text_file = "input.txt"

def load_data(input_text_file):
    with open(input_text_file) as input_file:
        data = []
        for index, line in enumerate(input_file):
            data.append(line.strip())
    return data

def scratch_the_card(card_contents):
    #card_contents = card.split(':')[1]

    winning_numbers = set(card_contents.split('|')[0].split())
    numbers_you_have = set(card_contents.split('|')[1].split())

    your_winning_numbers = winning_numbers & numbers_you_have

    return len(your_winning_numbers)

def scratch_the_cards(card_deck) -> list[str]:

    for card in card_deck :

        #this_card_score = scratch_the_card(card_deck[i+1]['contents'])
        this_card_score = scratch_the_card(card_deck[card]['contents'])

        for j in range(card+1, card+1+this_card_score):
            card_deck[j]['copies'] += card_deck[card]['copies']

    return card_deck

def build_the_deck(data):
    card_deck = {}
    for i, card in enumerate(data):
        id = int(card.split(':')[0].split()[1])
        card_deck[id] = {'copies': 1, 'contents': card.split(':')[1]}

    return card_deck

def add_up_all_the_copies(scratched_cards):
    total_card_count = 0
    for card in scratched_cards:
        total_card_count += scratched_cards[card]['copies']
    return total_card_count

if __name__ == '__main__':

    data = load_data(input_text_file)

    card_deck = build_the_deck(data)
    scratched_cards = scratch_the_cards(card_deck)

    total_deck = add_up_all_the_copies(scratched_cards)

    if input_text_file == "sample.txt":
        assert total_deck == 30

    print(f"{total_deck=}")

    #store answer as a comment
    #
    #