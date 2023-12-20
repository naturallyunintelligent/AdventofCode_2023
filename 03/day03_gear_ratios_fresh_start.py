from re import match

input_text_file = "sample.txt"
#input_text_file = "input.txt"

def load_data(input_text_file):
    with open(input_text_file) as input_file:
        data = []
        for index, line in enumerate(input_file):
            data.append(line.strip())
    return data


def extract_valid_part_numbers(data):
    symbol_coordinates = find_coordinates_of_symbols(data)

    for i, line in enumerate(data):
        for j, character in enumerate(line):
            if data[i,j]

    return [126, 456, 789]


if __name__ == '__main__':

    data = load_data(input_text_file)

    confirmed_part_numbers = extract_valid_part_numbers(data)

    sum_of_part_numbers = sum(confirmed_part_numbers)

    if input_text_file == "sample.txt":
        assert sum_of_part_numbers == 4361

    print(f"{sum_of_part_numbers=}")

    #store answer as a comment
    #
    #