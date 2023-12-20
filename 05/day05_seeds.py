
input_text_file = "sample.txt"
#input_text_file = "input.txt"

def load_data(input_text_file):
    with open(input_text_file) as input_file:
        data = []
        for index, line in enumerate(input_file):
            data.append(line.strip())
    return data



if __name__ == '__main__':

    data = load_data(input_text_file)

    answer =

    if input_text_file == "sample.txt":
        assert answer == 30

    print(f"{answer=}")

    #store answer as a comment
    #
    #