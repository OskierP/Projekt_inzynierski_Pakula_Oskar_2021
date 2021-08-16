#Made by Oskar Pakula
#Gdansk University of Technology
#Bachelor of Science - project

import numpy as np

def file_2_list(file, x: str):

    list = file.read().split("{}".format(x))

    return list


def Disperssion_range(n: int, epsilon, tau, alpha, freq: float):  #zakresy dyspersyjne w zależności od przyjetego modelu
    sigma = 0
    for i in range(0, n): #zakres od 1 do n. Należy pamiętać, iż programy liczą od zera (tablice)
        sigma = complex(sigma + (epsilon[i]/(1+(1j*2*np.pi*freq*tau[i])**(1-alpha[i]))))


def N_cole_cole(N: int, file_epsilon, file_tau, file_alpha, freq: float, epsiO, sig ):
    result = 0
    result = complex( Disperssion_range(N, file_epsilon, file_tau, file_alpha, freq) + (sig/(1j*2*np.pi*freq*epsiO)))


def main():
    '''
    Four_cole_cole = open('liczby.txt', 'r')
    #Two_cole_cole = open('liczby.txt', 'r')

    list_FCC=file_2_list(Four_cole_cole, ",")

    print(list_FCC)
'''
    #Disperssion_range(4, plik)
    x=complex((1+2/1j))
    y=4
    z= complex(x+y)

    print(z.imag)

if __name__ == '__main__':
    main()
#test czy działą
