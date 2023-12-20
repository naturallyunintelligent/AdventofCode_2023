from re import match

input_text_file = "sample.txt"
#input_text_file = "input.txt"

def load_data(input_text_file):
    with open(input_text_file) as input_file:
        data = []
        for index, line in enumerate(input_file):
            data.append(line.strip())
    return data


def build_working_matrix(i, data):
    current_matrix = []
    if i == 0:
        current_matrix.append('')
        current_matrix.append(data[i])
        current_matrix.append(data[i + 1])
    elif (i+1) == len(data):
        current_matrix.append(data[i-1])
        current_matrix.append(data[i])
        current_matrix.append('')
    else:
        current_matrix.append(data[i-1])
        current_matrix.append(data[i])
        current_matrix.append(data[i+1])
    return current_matrix

def split_the_matrix_lines(current_matrix):
    number_blocks = []
    for i, string in enumerate(current_matrix):

        #number_blocks.append(string.split(match('[0-9]+', string)))
        number_blocks.append(int(match('[0-9]+', string)))
    return number_blocks

def is_it_a_part_number_though(number_blocks, current_matrix):
    part_numbers = []
    for i, number in enumerate(number_blocks[1]):
        if match('[0-9]+', number):
            #if current_matrix[i-1:]
            part_numbers.append(number)
    return part_numbers

def parse_out_the_parts(data):
    valid_part_numbers = []
    for i, line in enumerate(data):
        current_matrix = build_working_matrix(i, data)
        number_blocks = split_the_matrix_lines(current_matrix)
        line_part_numbers = is_it_a_part_number_though(number_blocks, current_matrix)
        for part_number in line_part_numbers:
            valid_part_numbers.append(part_number)
    return valid_part_numbers


if __name__ == '__main__':

    data = load_data(input_text_file)

    valid_part_numbers = parse_out_the_parts(data)
    sum_of_part_numbers = sum(valid_part_numbers)

    if input_text_file == "sample.txt":
        assert sum_of_part_numbers == 4361

    print(f"{sum_of_part_numbers=}")

    #store answer as a comment
    #
    #