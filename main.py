# Made by Oskar Pakula
# Gdansk University of Technology
# Bachelor of Science - project
import csv

import constant as const
from Objects_2_Cole_Cole import Two_Cole_Cole_Objects as TCCO
from Objects_4_Cole_Cole import Four_Cole_Cole_Objects as FCCO
from file_functions_module import *
from plot_module import plot


def disperssion_range(n: int, epsilon, tau, alpha, freq: float):  # zakresy dyspersyjne
    sigma = 0

    for i in range(0, n):  # zakres od 1 do n. Należy pamiętać, iż programy liczą od zera (tablice)
        sigma = complex(sigma + (epsilon[i] / (1 + (1j * 2 * const.PI * freq * tau[i]) ** (1 - alpha[i]))))

    return sigma


def n_cole_cole(n: int, freq_bottom: int, freq_upper: int, list, step: int):
    array_tissue = []
    i = 0

    for tissue in list:
        array_tissue.append([])
        array_tissue[i].append(tissue.get_name())

        for freq in range(freq_bottom, freq_upper + step, step):
            result = complex(tissue.get_epsilon_inf() +
                             disperssion_range(
                                 n, tissue.get_epsilon(), tissue.get_tau(), tissue.get_alpha(), float(freq)
                             ) +
                             (tissue.get_sigma0() / (1j * 2 * const.PI * const.epsilon_0)))
            array_tissue[i].append(str(round(result.real, 3)))
        i += 1

    return array_tissue


def freq_for_plot(freq_bottom: int, freq_upper: int, step: int, files):
    array = ['frequency']

    for freqz in range(freq_bottom, freq_upper + step, step):
        array.append(freqz)

    with open(files, 'w') as file:
        for element in array:
            file.write(f'{element},')
    file.close()


def main():
    freq_bottom = 1 * 10 ** 6
    freq_upper = 26500 * 10 ** 6
    step = 1 * 10 ** 6

    # calculates values epsilon_r
    # list_2_file(n_cole_cole(4, freq_bottom, freq_upper, FCCO, step), 'testowy4.csv')
    # list_2_file(n_cole_cole(2, freq_bottom, freq_upper, TCCO, step), 'testowy2.csv')
    # freq_for_plot(freq_bottom, freq_upper, step, 'frequency.csv') #need to delete last ","

    # calculates values sigma
    #
    #

    freq = file_2_dict('frequency.csv', ',')
    four_cole_cole_dict = file_2_dict('testowy4.csv', ',')
    two_cole_cole_dict = file_2_dict('testowy2.csv', ',')

    # print(two_cole_cole_dict['frequency'].index(500000000))

    # Does not metter if we take four_cole_cole_dict or two_cole_cole_dict for frequency
    plot(freq['frequency'], four_cole_cole_dict['Dry_Skin'], two_cole_cole_dict['Skin'])


if __name__ == '__main__':
    np.set_printoptions(linewidth=150)
    main()

# test czy działą
