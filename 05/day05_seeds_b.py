import time
from re import match
from re import sub

#input_text_file = "sample.txt"
#input_text_file = "input_first_line.txt"
input_text_file = "input.txt"

class Map:
    def __init__(self, source_name, dest_name):
        self.source_name = source_name
        self.dest_name = dest_name
        self.map_locations = []




def load_data(input_text_file):
    print("load_data...")
    with open(input_text_file) as input_file:
        data = []
        for index, line in enumerate(input_file):
            data.append(line.strip())
    print("...load_data")
    return data

def find_next_seed(data):
    print("find_next_seed...")
    seeds = []
    range_values = data[0].split()[1:]
    for a, range_value in enumerate(range_values):
        range_values[a] = int(range_value)
    for i, value in enumerate(range_values):
        i = int(i)
        if i % 2 == 0:
            for seed_value in range(range_values[i], range_values[i]+range_values[i+1]):
                #seeds.append(seed_value)
                print(f"...find_next_seed {seed_value}")
                yield seed_value
        else:
            continue
    print("...find_next_seed False")
    yield False


def parse_almanac_to_maps(data):
    print("parse_almanac_to_maps...")
    # Dictionary to store maps
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



            name = current_map_name.split('-')
            source_name = name[0]
            dest_name = name[2].split()[0]


            # Dynamically create an instance of the class
            new_instance = Map(source_name, dest_name)

            # Store the instance in the dictionary with the lookup value as the key
            maps[current_map_name] = new_instance

            # Access the value attribute of the instance using the lookup value
            print(maps[current_map_name].source_name)
            print(maps[current_map_name].dest_name)
        else:
            row_values = line.split()
            maps[current_map_name].map_locations.append(row_values)

    print(f"...parse_almanac_to_maps {maps}")
    return maps

def lookup_map_next_value(initial_value, map_values):
    #print("lookup_map_final_value...")
    for row in map_values.map_locations:

        if initial_value in range(int(row[1]), int(row[1]) + int(row[2])):
            next_value = int(row[0]) + (initial_value - int(row[1]))
            return next_value
    next_value = initial_value
    print(f"...lookup_map_final_value {next_value}")
    return next_value

def follow_maps(A, initial_value, maps):
    print("follow_map...")

    B = ''

    for map in maps:
        if match(A, map):
            print(f"matched {A}, map: {map}")
            next_value = lookup_map_next_value(int(initial_value), maps[map])

            A = maps[map].dest_name
            initial_value = next_value
        else:
            print(f"something wrong, no match")
    B = maps[map].dest_name
    print(f"...follow_map {B}, {next_value}")
    return B, next_value


if __name__ == '__main__':

    tic = time.perf_counter()
    data = load_data(input_text_file)

    #parse almanac to list of maps
    maps = parse_almanac_to_maps(data)

    #generator to fetch next seed
    seed_gen = find_next_seed(data)

    #initialise
    min_seed_location = 0

    for seed_value in seed_gen:
        #continue until generator has generated a seed
        if seed_value == False:
            continue

        A = 'seed'
        B, final_value = follow_maps(A, seed_value, maps)
        assert B == 'location'

        #save only min location:
        if min_seed_location == 0:
            min_seed_location = final_value
            print(f">>>min_seed_location set as: {min_seed_location}")
        elif final_value < min_seed_location:
            min_seed_location = final_value
            print(f">>>New min_seed_location set as: {min_seed_location}")

    answer = min_seed_location

    if input_text_file == "sample.txt":
        #assert len(initial_seed_locations) == 27
        assert answer == 46

    toc = time.perf_counter()

    print(f"{answer=}")
    print(f"Solution in: {toc - tic:0.4f} seconds")

    #store answer as a comment
    #
    #