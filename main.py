# Made by Oskar Pakula
# Gdansk University of Technology
# Bachelor of Science - project

import constant as const
from file_functions_module import *
# from Objects_2_Cole_Cole import two_Cole_Cole_Objects as tCCO
# from Objects_4_Cole_Cole import four_Cole_Cole_Objects as fCCO
from plot_module import plot_all_tissue
from tissue_plots import tissue_plotting


def disperssion_range(n: int, epsilon, tau, alpha, freq: float):  # dispersion ranges
    sigma = 0

    for i in range(0, n):  # range from 1 to n, NOTE: first element is at index 0
        sigma = complex(sigma + (epsilon[i] / (1 + (1j * 2 * const.PI * freq * tau[i]) ** (1 - alpha[i]))))

    return sigma


def n_cole_cole(n: int, freq_bottom: int, freq_upper: int, list, step: int, real_or_imag):
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
                             (tissue.get_sigma0() / (1j * 2 * const.PI * const.EPSILON_0 * float(freq))))

            if real_or_imag:
                result = round(result.real, 3)
            else:
                result = round((-result.imag * 2 * const.PI * const.EPSILON_0 * freq), 5)

            array_tissue[i].append(str(result))

        i += 1

    return array_tissue


def freq_for_plot(freq_bottom: int, freq_upper: int, step: int, files):
    array = ['frequency']

    for freqz in range(freq_bottom, freq_upper + step, step):
        array.append(freqz)

    with open(files, 'w') as file:
        file.write(array[0])
        for element in array[1:]:
            file.write(f',{element}')
    file.close()


def main():
    # frequencies
    # uncomment when using list_2_file
    freq_bottom = 1 * 10 ** 6
    freq_upper = 26500 * 10 ** 6
    step = 100 * 10 ** 3

    # uncomment when using plot_all_tissue
    freq_bottom_tcc = 500 * 10 ** 6
    freq_upper_fcc = 10 * 10 ** 9

    # calculates values epsilon_r
    # list_2_file(n_cole_cole(4, freq_bottom, freq_upper, fCCO, step, True), 'epsilon_fcc.csv')
    # list_2_file(n_cole_cole(2, freq_bottom, freq_upper, tCCO, step, True), 'epsilon_tcc.csv')

    # calculates values sigma
    # list_2_file(n_cole_cole(4, freq_bottom, freq_upper, fCCO, step, False), 'sigma_fcc.csv')
    # list_2_file(n_cole_cole(2, freq_bottom, freq_upper, tCCO, step, False), 'sigma_tcc.csv')

    # adds values for the x axis
    # freq_for_plot(freq_bottom, freq_upper, step, 'frequency.csv')

    # for frequency
    freq = file_2_dict('frequency.csv', ',')

    # for epsilon_r
    four_cole_cole_dict_epsilon = file_2_dict('epsilon_fcc.csv', ',')
    two_cole_cole_dict_epsilon = file_2_dict('epsilon_tcc.csv', ',')

    # for sigma
    four_cole_cole_dict_sigma = file_2_dict('sigma_fcc.csv', ',')
    two_cole_cole_dict_sigma = file_2_dict('sigma_tcc.csv', ',')

    # tissue plotting - groups of tissues
    tissue_plotting(freq['frequency'], four_cole_cole_dict_epsilon, four_cole_cole_dict_sigma,
                    two_cole_cole_dict_epsilon, two_cole_cole_dict_sigma)

    # tissue plotting - one plot, one model
    plot_all_tissue(freq['frequency'], two_cole_cole_dict_epsilon, two_cole_cole_dict_sigma, freq_bottom_tcc)
    plot_all_tissue(freq['frequency'], four_cole_cole_dict_epsilon, four_cole_cole_dict_sigma, freq_upper_fcc)


if __name__ == '__main__':
    np.set_printoptions(linewidth=150)
    main()
