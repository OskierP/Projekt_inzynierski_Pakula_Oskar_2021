import matplotlib.pyplot as mp


def find_index(dictionary, frequency):
    return dictionary.index(frequency)


def plot_all_tissue(x, model1, model2, freq: int):
    start = 1
    stop = -1
    tmp = 10 * 10 ** 9

    fig, (epsilon_r, sigma) = mp.subplots(2, sharex=True)

    if freq == tmp:
        stop = find_index(x[1:], freq)
    else:
        start = find_index(x[1:], freq)

    for i in model1:
        epsilon_r.plot(x[start:stop], model1[i][start:stop], label=model1[i][0])
        sigma.plot(x[start:stop], model2[i][start:stop], label=model2[i][0])

        sigma.legend(loc='right', ncol=1, bbox_to_anchor=(1.13, 1), fontsize=7)

    epsilon_r.set_title('Relative permittivity')
    epsilon_r.set_ylabel('\u03B5r')
    epsilon_r.set_yscale('log')
    epsilon_r.grid()
    epsilon_r.grid(which='minor', alpha=0.15)

    sigma.set_title('Sigma')
    sigma.set_ylabel('\u03C3 [S/m]')
    sigma.set_yscale('log')
    sigma.grid()
    sigma.grid(which='minor', alpha=0.15)

    mp.xlabel('Frequency [Hz]')
    mp.xscale('log')

    mp.show()


def plot(x, file_name: str, fcc_model='', tcc_model='', cc_model1='', model1='', cc_model2='', model2=''):
    fig, (epsilon_r, sigma) = mp.subplots(2, sharex=True)

    width_fcc1 = 2
    width_fcc2 = 2
    width_tcc = 2

    five_hundred_MHz = 500 * 10 ** 6
    ten_GHz = 10 * 10 ** 9

    index_500MHz = find_index(x, five_hundred_MHz)
    index_10GHz = find_index(x, ten_GHz)

    for graph, ind in (epsilon_r, 0), (sigma, 1):

        if fcc_model != '':
            graph.plot(x[1:index_10GHz - 1], fcc_model[ind][1:index_10GHz - 1],
                       label=fcc_model[ind][0] + ': 4-Cole-Cole',
                       color='forestgreen',
                       linewidth=width_fcc1)
            graph.plot(x[index_10GHz - 1:], fcc_model[ind][index_10GHz - 1:], linestyle='dotted', color='forestgreen',
                       linewidth=width_fcc1)

        if cc_model1 != '':

            if model1 == '2':
                graph.plot(x[index_500MHz - 1:], cc_model1[ind][index_500MHz - 1:],
                           label=cc_model1[ind][0] + ': 2-Cole-Cole', color='tab:blue',
                           linewidth=width_tcc)
                graph.plot(x[1:index_500MHz - 1], cc_model1[ind][1:index_500MHz - 1], color='tab:blue',
                           linestyle='dotted', linewidth=width_tcc)

            elif model1 == '4':
                graph.plot(x[1:index_10GHz - 1], cc_model1[ind][1:index_10GHz - 1],
                           label=cc_model1[ind][0] + ': 4-Cole-Cole', color='tab:blue',
                           linewidth=width_fcc2)
                graph.plot(x[index_10GHz - 1:], cc_model1[ind][index_10GHz - 1:], linestyle='dotted', color='tab:blue',
                           linewidth=width_fcc2)

        if tcc_model != '':
            color = 'r'
            if fcc_model == '' and cc_model1 == '':
                color = 'tab:blue'
            graph.plot(x[index_500MHz - 1:], tcc_model[ind][index_500MHz - 1:],
                       label=tcc_model[ind][0] + ': 2-Cole-Cole', color=color,
                       linewidth=width_tcc)
            graph.plot(x[1:index_500MHz - 1], tcc_model[ind][1:index_500MHz - 1], color=color,
                       linestyle='dotted', linewidth=width_tcc)

        if cc_model2 != '':
            if model2 == '2':
                graph.plot(x[index_500MHz - 1:], cc_model2[ind][index_500MHz - 1:],
                           label=cc_model2[ind][0] + ': 2-Cole-Cole', color='forestgreen',
                           linewidth=width_tcc)
                graph.plot(x[1:index_500MHz - 1], cc_model2[ind][1:index_500MHz - 1], color='forestgreen',
                           linestyle='dotted', linewidth=width_tcc)

            elif model2 == '4':
                graph.plot(x[1:index_10GHz - 1], cc_model2[ind][1:index_10GHz - 1],
                           label=cc_model2[ind][0] + ': 4-Cole-Cole', color='tab:orange',
                           linewidth=width_fcc2)
                graph.plot(x[index_10GHz - 1:], cc_model2[ind][index_10GHz - 1:], linestyle='dotted',
                           color='tab:orange',
                           linewidth=width_fcc2)

    epsilon_r.set_title('Relative permittivity')
    epsilon_r.set_ylabel('\u03B5r')
    epsilon_r.set_yscale('log')
    epsilon_r.legend()
    epsilon_r.grid()
    epsilon_r.grid(which='minor', alpha=0.15)

    sigma.set_title('Sigma')
    sigma.set_ylabel('\u03C3 [S/m]')
    sigma.set_yscale('log')
    sigma.grid()
    sigma.grid(which='minor', alpha=0.15)

    mp.xlabel('Frequency [Hz]')
    mp.xscale('log')

    mp.savefig(f'plot_of_{file_name}.png', dpi=600)
    # mp.show()
    mp.close()
