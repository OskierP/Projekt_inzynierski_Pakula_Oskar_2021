import numpy as np

def file_2_list(file, x: str):
    Array = []
    Array.append([])
    index = 0

    for element in file.read().split(f"{x}"):

        if '\n' in element:
            tmp = element.split('\n')
            Array[index].append(tmp[0])
            Array.append([])
            index += 1
            Array[index].append(tmp[1])
        else:
            Array[index].append(element)

    return Array

def show_list(list):
    return np.array(list)