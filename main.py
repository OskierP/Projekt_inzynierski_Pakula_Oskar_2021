# Made by Oskar Pakula
# Gdansk University of Technology
# Bachelor of Science - project

import constant as const
from Objects_4_Cole_Cole import Four_Cole_Cole_Objects as FCCO
from file_2_list import *


def disperssion_range(n: int, epsilon, tau, alpha,
                      freq: float):  # zakresy dyspersyjne w zależności od przyjetego modelu
    sigma = 0

    for i in range(0, n):  # zakres od 1 do n. Należy pamiętać, iż programy liczą od zera (tablice)
        sigma = complex(sigma + (epsilon[i] / (1 + (1j * 2 * const.PI * freq * tau[i]) ** (1 - alpha[i]))))

    return sigma


def n_cole_cole(n: int, freq_bottom: int, freq_upper: int, list, step: int):
    array = [['tissue']]
    i = 1

    for freqz in range(freq_bottom, freq_upper + step, step):
        array[0].append(str(freqz))

    for tissue in list:
        array.append([])
        array[i].append(tissue.get_name())
        for freq in range(freq_bottom, freq_upper + step, step):
            result = complex(tissue.get_epsilon_inf() + disperssion_range(n, tissue.get_epsilon(), tissue.get_tau(),
                                                                          tissue.get_alpha(), float(freq)) + (
                                     tissue.get_sigma0() / (1j * 2 * const.PI * const.epsilon_0)))
            array[i].append(str(result))
        i += 1

    return array


def main():
    freq_4_cc_bottom = 1 * 10 ** 6
    freq_4_cc_upper = 10 * 10 ** 9
    step = 10000 * 10 ** 6

    # CC4 = file_2_list(open('Cole-Cole_4.csv', 'r'), ",") # 4-Cole-cole: czytanie watości z pliku csv
    # CC2 = file_2_list(open('Cole-Cole_2.csv', 'r'), ",") # 2-Cole-cole: czytanie watości z pliku csv

    # print(np.array(CC4))
    # print('\n')
    # print(np.array(CC2))
    # print(FCCO[0].get_tau())
    # print(TCCO[1].get_name())
    # print(FCCO[1].get_sigma0())
    # print(FCCO[1].get_epsilon_inf())
    # print(show_list(FCC))
    # print(epsilon(CC2,0,2))
    # print(tau(CC2,0,2))
    # print(alpha(CC2,0,2))
    # Disperssion_range(4, plik)
    # x=complex((1+2/1j))
    # y=4
    # z= complex(x+y)
    # print(z.imag)

    list_2_file(n_cole_cole(4, freq_4_cc_bottom, freq_4_cc_upper, FCCO, step), 'testowy4.csv')


if __name__ == '__main__':
    np.set_printoptions(linewidth=150)
    main()

# test czy działą
