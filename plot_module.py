import matplotlib.pyplot as mp


def find_index(dict, frequency):
    return dict.index(frequency)


def plot(x, file_name: str, fcc_model1='', tcc_model='', cc_model1='', model1='', cc_model2='', model2=''):
    fig, (epsilon_r, sigma) = mp.subplots(2, sharex=True)

    width_fcc1 = 2
    width_fcc2 = 2
    width_tcc = 2

    five_hundred_MHz = 500 * 10 ** 6
    ten_GHz = 10 * 10 ** 9

    index_500MHz = find_index(x, five_hundred_MHz)
    index_10GHz = find_index(x, ten_GHz)

    for graph, ind in (epsilon_r, 0), (sigma, 1):
        if fcc_model1 !='':
            graph.plot(x[1:index_10GHz - 1], fcc_model1[ind][1:index_10GHz - 1], label=fcc_model1[ind][0] + ': 4-Cole-Cole',
                   color='g',
                   linewidth=width_fcc1)

        if tcc_model != '':
            graph.plot(x[index_500MHz - 1:], tcc_model[ind][index_500MHz - 1:],
                       label=tcc_model[ind][0] + ': 2-Cole-Cole', color='orange',
                       linewidth=width_tcc)

        if fcc_model1 != '':
            graph.plot(x[index_10GHz - 1:], fcc_model1[ind][index_10GHz - 1:], linestyle='dotted', color='g',
                   linewidth=width_fcc1)

        if cc_model1 != '':
            if model1 == '2':
                graph.plot(x[index_500MHz - 1:], cc_model1[ind][index_500MHz - 1:],
                           label=cc_model1[ind][0] + ': 2-Cole-Cole', color='b',
                           linewidth=width_tcc)
                graph.plot(x[1:index_500MHz - 1], cc_model1[ind][1:index_500MHz - 1], color='b',
                           linestyle='dotted', linewidth=width_tcc)

            elif model1 == '4':
                graph.plot(x[1:index_10GHz - 1], cc_model1[ind][1:index_10GHz - 1],
                       label=cc_model1[ind][0] + ': 4-Cole-Cole', color='b',
                       linewidth=width_fcc2)
                graph.plot(x[index_10GHz - 1:], cc_model1[ind][index_10GHz - 1:], linestyle='dotted', color='b',
                       linewidth=width_fcc2)

        if tcc_model !='':
            graph.plot(x[1:index_500MHz - 1], tcc_model[ind][1:index_500MHz - 1], color='orange',
                   linestyle='dotted', linewidth=width_tcc)

        if cc_model2 !='':
            if model2 == '2':
                graph.plot(x[index_500MHz - 1:], cc_model2[ind][index_500MHz - 1:],
                           label=cc_model2[ind][0] + ': 2-Cole-Cole', color='r',
                           linewidth=width_tcc)
                graph.plot(x[1:index_500MHz - 1], cc_model2[ind][1:index_500MHz - 1], color='r',
                           linestyle='dotted', linewidth=width_tcc)

            elif model2 == '4':
                graph.plot(x[1:index_10GHz - 1], cc_model2[ind][1:index_10GHz - 1],
                           label=cc_model2[ind][0] + ': 4-Cole-Cole', color='r',
                           linewidth=width_fcc2)
                graph.plot(x[index_10GHz - 1:], cc_model2[ind][index_10GHz - 1:], linestyle='dotted', color='r',
                           linewidth=width_fcc2)

    epsilon_r.set_title('Relative permittivity')
    epsilon_r.set_ylabel('\u03B5r')
    epsilon_r.set_yscale('log')
    epsilon_r.legend()

    sigma.set_ylabel('\u03C3 [S/m]')
    sigma.set_title('Sigma')
    sigma.set_yscale('log')

    mp.xlabel('Frequency [Hz]')
    mp.xscale('log')

    mp.savefig(f'plot_of_{file_name}.png', dpi=600)
    mp.show()
