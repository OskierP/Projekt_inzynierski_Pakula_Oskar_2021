#Made by Oskar Pakula
#Gdansk University of Technology
#Bachelor of Science - project



def file_2_list(file, x: str):

    list = file.read().split("{}".format(x))

    return list




def Disperssion_range(n: int, file):  #zakresy dyspersyjne w zależności od przyjetego modelu
    for i in range(0, n): #zakres od 1 do n. Należy pamiętać, iż programy liczą od zera (tablice)
        print('s')


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

