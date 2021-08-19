import matplotlib.pyplot as mp


def find_index(dict, frequency):
    return dict.index(frequency)


def plot(x, fcc_model1, tcc_model, fcc_model2=''):
    width_fcc1 = 2
    width_fcc2 = 2
    width_tcc = 2

    five_hundred_MHz = 500 * 10 ** 6
    ten_GHz = 10 * 10 ** 9

    index_500MHz = find_index(x, five_hundred_MHz)
    index_10GHz = find_index(x, ten_GHz)

    mp.plot(x[1:index_10GHz - 1], fcc_model1[1:index_10GHz - 1], label=fcc_model1[0], color='g', linewidth=width_fcc1)

    mp.plot(x[index_500MHz - 1:], tcc_model[index_500MHz - 1:], color='orange', linewidth=width_tcc)

    mp.plot(x[index_10GHz - 1:], fcc_model1[index_10GHz - 1:], linestyle='dotted', color='g', linewidth=width_fcc1)

    if fcc_model2 != '':
        mp.plot(x[1:index_10GHz - 1], fcc_model2[1:index_10GHz - 1], label=fcc_model2[0], color='b',
                linewidth=width_fcc2)
        mp.plot(x[index_10GHz - 1:], fcc_model2[index_10GHz - 1:], linestyle='dotted', color='b', linewidth=width_fcc2)

    mp.plot(x[1:index_500MHz - 1], tcc_model[1:index_500MHz - 1], label=tcc_model[0], color='orange',
            linestyle='dotted', linewidth=width_tcc)

    mp.xscale('log')
    mp.xlabel('Frequency [Hz]')

    mp.yscale('log')
    mp.ylabel('Epsilon [Er]')
    mp.title('Relative permittivity')

    mp.legend()
    mp.show()
