import csv

import numpy as np


def file_2_list(file, x: str):
    array = [[]]
    # array.append([])
    index = 0

    for element in file.read().split(f"{x}"):

        if '\n' in element:
            tmp = element.split('\n')
            array[index].append(tmp[0])
            array.append([])
            index += 1
            array[index].append(tmp[1])
        else:
            array[index].append(element)

    return array


def show_list(list):
    return np.array(list)


def list_2_file(list, file):
    csv_writer = csv.writer(open(file, 'w'))
    csv_writer.writerows(list)
