input_text_file = "sample.txt"
#input_text_file = "input.txt"

def load_data(input_text_file):
    with open(input_text_file) as input_file:
        data = []
        for index, line in enumerate(input_file):
            data.append(line.strip())
    return data


def some_random_function(data):


    return True


if __name__ == '__main__':

    data = load_data(input_text_file)

    sum_of_part_numbers = some_random_function(data)


    if input_text_file == "sample.txt":
        assert sum_of_part_numbers == 4361

    print(f"{sum_of_part_numbers=}")

    #store answer as a comment
    #
    #