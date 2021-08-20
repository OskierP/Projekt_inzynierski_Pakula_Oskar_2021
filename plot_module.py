import matplotlib.pyplot as mp


def find_index(dict, frequency):
    return dict.index(frequency)


def plot(x, fcc_model1, tcc_model, fcc_model2=''):
    fig, (epsilon_r, sigma) = mp.subplots(2, sharex = True)

    width_fcc1 = 2
    width_fcc2 = 2
    width_tcc = 2

    five_hundred_MHz = 500 * 10 ** 6
    ten_GHz = 10 * 10 ** 9

    index_500MHz = find_index(x, five_hundred_MHz)
    index_10GHz = find_index(x, ten_GHz)



    for graph, ind in (epsilon_r, 0), (sigma, 1):
        graph.plot(x[1:index_10GHz - 1], fcc_model1[ind][1:index_10GHz - 1], label=fcc_model1[ind][0], color='g',
                       linewidth=width_fcc1)

        graph.plot(x[index_500MHz - 1:], tcc_model[ind][index_500MHz - 1:], label=tcc_model[ind][0], color='orange',
                       linewidth=width_tcc)

        graph.plot(x[index_10GHz - 1:], fcc_model1[ind][index_10GHz - 1:], linestyle='dotted', color='g',
                       linewidth=width_fcc1)

        if fcc_model2 != '':
            graph.plot(x[1:index_10GHz - 1], fcc_model2[ind][1:index_10GHz - 1], label=fcc_model2[ind][0], color='b',
                           linewidth=width_fcc2)
            graph.plot(x[index_10GHz - 1:], fcc_model2[ind][index_10GHz - 1:], linestyle='dotted', color='b',
                           linewidth=width_fcc2)

        graph.plot(x[1:index_500MHz - 1], tcc_model[ind][1:index_500MHz - 1], color='orange',
                       linestyle='dotted', linewidth=width_tcc)

    epsilon_r.set_title('Relative permittivity')
    epsilon_r.set_ylabel('Epsilon [Er]')
    epsilon_r.set_yscale('log')
    epsilon_r.legend()

    sigma.set_ylabel('Sigma [6]')
    sigma.set_title('Sigma')
    sigma.set_yscale('log')
    sigma.legend()

    mp.xlabel('Frequency [Hz]')
    mp.xscale('log')

    # mp.ylabel('Epsilon [Er]')
    # mp.title('Relative permittivity')

    mp.show()
