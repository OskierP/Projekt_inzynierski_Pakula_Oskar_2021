import csv

import numpy as np


# functions for file operations

def file_2_list(file, character: str):
    array = [[]]
    # array.append([])
    index = 0

    for element in file.read().split(f"{character}"):

        if '\n' in element:
            tmp = element.split('\n')
            array[index].append(tmp[0])
            array.append([])
            index += 1
            array[index].append(tmp[1])
        else:
            array[index].append(element)

    file.close()
    return array


def show_list(list):
    return np.array(list)


def list_2_file(list, file):
    csv_writer = csv.writer(open(file, 'w'))
    csv_writer.writerows(list)
    # file.close()


def str_2_float_list(list):
    for element in list:
        for i in range(1, len(element)):
            element[i] = float(element[i])


def file_2_dict(file, character: str):
    tmp_dict = {}

    tmp_array = file_2_list(open(file, 'r'), character)

    str_2_float_list(tmp_array)

    for element in tmp_array:
        tmp_dict[element[0]] = element[0:]

    return tmp_dict
