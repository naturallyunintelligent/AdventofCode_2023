from re import sub


#input_text_file = "sample.txt"
input_text_file = "input.txt"

def load_data(input_text_file):
    with open(input_text_file) as input_file:
        data = []
        for index, line in enumerate(input_file):
            data.append(line.strip())
    return data


def sum_cal_values(cal_values):
    total_cal_value = sum(cal_values)

    return total_cal_value

def remove_letters(data):
    cal_values = []
    for line in data:
        numeric_line = sub("[^0-9]", "", line)
        cal_value = numeric_line[0]+numeric_line[-1]
        cal_values.append(int(cal_value))

    return cal_values

if __name__ == '__main__':

    data = load_data(input_text_file)

    cal_values = remove_letters(data)

    total_cal_value = sum_cal_values(cal_values)

    if input_text_file == "sample.txt":
        assert total_cal_value == 142

    print(f"total_cal_value: {total_cal_value}")

    #store answer as a comment
    #
    #54927