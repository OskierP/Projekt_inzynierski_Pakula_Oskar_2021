import matplotlib.pyplot as mp
import file_functions_module as ffm
import numpy as np


def find_index(dict, frequency):
    return dict.index(frequency)


def plot(x, fcc_model1, tcc_model, fcc_model2=''):

    mp.plot(x[1:], fcc_model1[1:], label=fcc_model1[0])
    # mp.plot(x_fcc[9:20], fcc_model1[9:20], color='r')
    mp.plot(x[1:], tcc_model[1:], label=tcc_model[0])

    if fcc_model2 != '':
        mp.plot(x[1:], fcc_model2[1:], label=fcc_model2[0])

    mp.xscale('log')
    mp.xlabel('Frequency [Hz]')

    mp.yscale('log')
    mp.ylabel('Epsilon [Er]')
    mp.title('Relative permittivity')

    mp.legend()
    mp.show()
