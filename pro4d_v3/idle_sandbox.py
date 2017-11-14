import main_01

list_data = main_01.load_from_file("damacai_1997_01_248_m.txt")

nr3drawSet = main_01.nr_3drawSet(list_data, 1, 1, 1)

nr_counter_list = main_01.counter_list_3draw(nr3drawSet)

sample_data = [6, 4, 8, 0, 3, 5, 0, 5]


def gen_pattern_given_count(list_count_data):
    # params: list containing patter count
    # sample of input = [6, 4, 8, 0, 3, 5, 0, 5...
    # output = a dictionary. key = count, value = [patterns]

    dict_counter_pattern = {}
    counter = 0
    while counter < len(sample_data):
        str_index = str(counter)
        while (len(str_index) < 3):
            str_index = "0" + str_index

        pattern_count = sample_data[counter]

        if pattern_count in dict_counter_pattern:
            dict_counter_pattern[pattern_count].append(str_index)
        else:
            dict_counter_pattern[pattern_count] = [str_index]
        counter += 1

    return dict_counter_pattern


print(sample_data)
print(dict_counter_pattern)
print
print
print("#####################################")
print ("#####    END OF EXECUTION       #####")
print("#####################################")


