#Made by Oskar Pakula
#Gdansk University of Technology
#Bachelor of Science - project

import numpy as np

from Objects_2_Cole_Cole import Two_Cole_Cole_Objects as TCCO
from Objects_4_Cole_Cole import FCC
from Objects_4_Cole_Cole import Four_Cole_Cole_Objects as FCCO
from file_2_list import show_list


def Disperssion_range(n: int, epsilon, tau, alpha, freq: float):  #zakresy dyspersyjne w zależności od przyjetego modelu
    sigma = 0

    for i in range(0, n): #zakres od 1 do n. Należy pamiętać, iż programy liczą od zera (tablice)
        sigma = complex(sigma + (epsilon[i]/(1+(1j*2*np.pi*freq*tau[i])**(1-alpha[i]))))


def N_cole_cole(N: int, material: int, freq_bottom: int, freq_upper: int, list):
    result = 0

    for i in range(len(list)):
        for j in range(freq_bottom, freq_upper):


            print('s')


    result = complex( Disperssion_range(N, file_epsilon, file_tau, file_alpha, freq) + (sig/(1j*2*np.pi*freq*epsiO)))


def main():
    # CC4 = file_2_list(open('Cole-Cole_4.csv', 'r'), ",") # 4-Cole-cole: czytanie watości z pliku csv
    # CC2 = file_2_list(open('Cole-Cole_2.csv', 'r'), ",") # 2-Cole-cole: czytanie watości z pliku csv

    # print(np.array(CC4))
    # print('\n')
    # print(np.array(CC2))
    print(FCCO[0].get_tau())
    print(TCCO[1].get_name())
    print(FCCO[1].get_sigma())
    print(FCCO[1].get_epsilon_inf())
    print(show_list(FCC[1]))
    # print(epsilon(CC2,0,2))
    # print(tau(CC2,0,2))
    # print(alpha(CC2,0,2))
    # Disperssion_range(4, plik)
    # x=complex((1+2/1j))
    # y=4
    # z= complex(x+y)
    #print(z.imag)


if __name__ == '__main__':
    np.set_printoptions(linewidth=150)
    main()

#test czy działą
