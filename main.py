#Made by Oskar Pakula
#Gdansk University of Technology
#Bachelor of Science - project

import numpy as np
import csv


def file_2_list(file, x: str):

    #list = file.read().split(f"{x}")

    Array =[]
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


def Disperssion_range(n: int, epsilon, tau, alpha, freq: float):  #zakresy dyspersyjne w zależności od przyjetego modelu
    sigma = 0
    for i in range(0, n): #zakres od 1 do n. Należy pamiętać, iż programy liczą od zera (tablice)
        sigma = complex(sigma + (epsilon[i]/(1+(1j*2*np.pi*freq*tau[i])**(1-alpha[i]))))


def N_cole_cole(N: int, file_epsilon, file_tau, file_alpha, freq: float, epsiO, sig ):
    result = 0
    result = complex( Disperssion_range(N, file_epsilon, file_tau, file_alpha, freq) + (sig/(1j*2*np.pi*freq*epsiO)))


def main():



    FCC4 = file_2_list(open('Cole-Cole_4.csv', 'r'), ",") # 4-Cole-cole: czytanie watości z pliku csv
    FCC2 = file_2_list(open('Cole-Cole_2.csv', 'r'), ",") # 2-Cole-cole: czytanie watości z pliku csv

    np.set_printoptions(linewidth=150)
    print(np.array(FCC4))
    print('\n')
    print(np.array(FCC2))

    # Disperssion_range(4, plik)
    # x=complex((1+2/1j))
    # y=4
    # z= complex(x+y)
    #print(z.imag)

if __name__ == '__main__':
    main()
#test czy działą
