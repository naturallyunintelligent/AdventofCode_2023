import time
from re import match
from re import sub

#input_text_file = "sample.txt"
#input_text_file = "input_first_line.txt"
input_text_file = "input.txt"

def load_data(input_text_file):
    with open(input_text_file) as input_file:
        data = []
        for index, line in enumerate(input_file):
            data.append(line.strip())
    return data

def find_next_seed(data):
    seeds = []
    range_values = data[0].split()[1:]
    for a, range_value in enumerate(range_values):
        range_values[a] = int(range_value)
    for i, value in enumerate(range_values):
        i = int(i)
        if i % 2 == 0:
            for seed_value in range(range_values[i], range_values[i]+range_values[i+1]):
                #seeds.append(seed_value)
                yield seed_value
        else:
            continue
    yield False


def parse_almanac_to_maps(data):
    maps = {}
    current_map_name = ''
    for line in data:
        if match('seeds:', line):
            continue
        elif line == '':
            continue
        elif match('\S+ map:', line):
            maps[line[:-1]] = []
            current_map_name = line[:-1]
        else:
            maps[current_map_name].append(line)
    return maps

def lookup_map_final_value(initial_value, map_values):
    for row in map_values:
        row_values = row.split()
        if initial_value in range(int(row_values[1]), int(row_values[1]) + int(row_values[2])):
            final_value = int(row_values[0]) + (initial_value - int(row_values[1]))
            return final_value
    final_value = initial_value
    return final_value

def extract_name_B(key):
    name = key.split('-')
    return name[2].split()[0]

def follow_map(A, initial_value, maps):
    B = ''

    for map in maps:
        if match(A, map):
            final_value = lookup_map_final_value(int(initial_value), maps[map])
            B = extract_name_B(map)
            A = B
            initial_value = final_value
        else:
            final_value = 'huh?'
            B = 'errrrr'

    return B, final_value


if __name__ == '__main__':

    tic = time.perf_counter()
    data = load_data(input_text_file)

    #parse almanac to list of seeds and maps
    #seeds = lookup_seeds(data)
    maps = parse_almanac_to_maps(data)
    initial_seed_locations = []
    seed_gen = find_next_seed(data)

    for seed_value in seed_gen:
        #     map through to location
        if seed_value == False:
            continue
        A = 'seed'
        #for map in maps:
        B, final_value = follow_map(A, seed_value, maps)
        assert B == 'location'
        #     append to the initial locations list
        initial_seed_locations.append(final_value)
        #seed_value = next(seed_value)
    answer = min(initial_seed_locations)

    if input_text_file == "sample.txt":
        assert len(initial_seed_locations) == 27
        assert answer == 46

    toc = time.perf_counter()

    print(f"{answer=}")
    print(f"Solution in: {toc - tic:0.4f} seconds")

    #store answer as a comment
    #
    #