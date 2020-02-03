from math import sqrt
from colorama import Back, Fore, Style, init
import matplotlib.pyplot as plt
import numpy as np
init(autoreset=True)

def saludo():
    print(Back.RED +Fore.CYAN +'Proyecto: Permeabilidad de los solidos por gases mediante difusión en estado estacionario')
    print(Fore.BLUE +'Integrantes:')
    print(Fore.GREEN +'Paula M. Bueno')
    print(Fore.GREEN +'Rubén J. Romo')

def valores_iniciales():
    global solubilidad_hidrogeno
    global presion1
    global area
    global espesor
    global difusividad_hidrogeno
    global densidad_niquel

    print(Fore.CYAN +'Opción 1 seleccionada. \nSe calculará la cantidad de centímetros cúbicos por segundo que se difundirá a través del níquel')

    temperatura= int(input('Ingrese temperatura [°C] de operación: '))
    presion1= float(input('Ingrese presión [atm] de operación: '))
    area= float(input('Ingrese área [cm2] del disco de níquel: '))
    espesor= float(input('Ingrese espesor [mm] del disco de níquel: '))
    solubilidad_hidrogeno= float(input('Ingrese solubilidad [cm3/g] del hidrógeno en níquel a 1 atm de presión y a %0.2f °C: '%temperatura))
    difusividad_hidrogeno= float(input('Ingrese difusividad [cm2/s] del hidrógeno en níquel a  %0.2f °C: '%temperatura))
    densidad_niquel= float(input('Ingrese densidad del níquel [g/cm3] a  %0.2f °C: '%temperatura))

def calculark(solubilidad,densidad):
    return solubilidad*densidad


def calcularjaz(difusividad,k,presion,espesor):
    return (difusividad*k*sqrt(presion))/(espesor/10)


def calcularwa(ja,area):
    wa=ja*area
    return wa

def calcularwah(ja,area):
    wa=ja*area/3600
    return wa
    

while True:
    saludo()
    opcion=str(input("Seleccione número de opción \n1) Calcular difusión molecular a través del níquel: \n2) Si es reacción heterogenea: \n3) Si es reacción homogenea: \n4) Si es placas planas:  \n5) Si es evaporación: \n6) Graficar difusión vs área: \n7) Graficar difusión vs presión: \n100) Para calificar directamente con 100 a los integrantes: "))
    if opcion=='1':
        valores_iniciales()
        print('A 1 atm Ca1 = k*sqrt(Pa)')
        print(Fore.MAGENTA +'El valor de k es: %0.6f' %calculark(solubilidad_hidrogeno,densidad_niquel), Fore.BLUE +'sqrt(atm)')
        print(Fore.MAGENTA +'El valor de Jaz es: %0.6f ' %calcularjaz(difusividad_hidrogeno,calculark(solubilidad_hidrogeno,densidad_niquel),presion1,espesor), Fore.BLUE + 'cm/s')
        print(Fore.MAGENTA +'El valor Wa es: %0.6f'  %calcularwa(calcularjaz(difusividad_hidrogeno,calculark(solubilidad_hidrogeno,densidad_niquel),presion1,espesor),area), Fore.BLUE + 'cm3/s')
        print(Fore.MAGENTA +'El valor Wa es: %0.6f' %calcularwah(calcularjaz(difusividad_hidrogeno, calculark(solubilidad_hidrogeno, densidad_niquel), presion1, espesor),area), Fore.BLUE + 'cm3/hora')
    elif opcion == '6':
        rango = range(int(input('Ingrese rango de area: ')))
        rangos = []
        was = []
        for x in rango:
            rangos.append(x)
            was.append(calcularwa(calcularjaz(difusividad_hidrogeno,calculark(solubilidad_hidrogeno,densidad_niquel),presion1,espesor),x))
        plt.plot(was,rangos,'r*')
        plt.xlabel('Difusión de hidrógeno')
        plt.ylabel('Area [cm2] ')
        plt.show()
    elif opcion == '7':
        rangop = range(int(input('Ingrese rango de presión [atm]: ')))
        rangos = []
        was = []
        for x in rangop:
            rangos.append(x)
            was.append(calcularwa(calcularjaz(difusividad_hidrogeno,calculark(solubilidad_hidrogeno,densidad_niquel),x,espesor),area))
        plt.plot(was,rangos,'g*')
        plt.xlabel('Difusión de hidrógeno')
        plt.ylabel('presión [atm] ')
        plt.show()
    elif opcion=='100':
        print(Style.BRIGHT + Fore.GREEN +'MUCHAS GRACIAS PROFESORA')
