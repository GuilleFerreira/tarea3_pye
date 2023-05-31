from scipy.stats import binom
from scipy.stats import geom
from scipy.stats import poisson
import statistics
import matplotlib.pyplot as plt
import numpy as np

# Distribución 1: binomial de parámetros n = 100, p = 0,35.
def generarDistribucionBinomial(size):
    return binom.rvs(100,0.35,size = size)

#Distribución 2: geométrica de parámetro p = 0,08
def generarDistribucionGeometrica(size):
    return geom.rvs(0.08,size = size)

#Distribución 3: poisson de parámetro λ = 30.
def generarDistribucionPoisson(size):
    return poisson.rvs(30,size = size)

#Variables teóricas
def variablesTeoricas():
    distribucion1Esperanza = 100*0.35
    distribucion1Varianza = 100*0.35*(1-0.35)
    distribucion2Esperanza = 1/0.08
    distribucion2Varianza = (1-0.08)/(0.08**2)
    distribucion3Esperanza = 30
    distribucion3Varianza = 30

    print("==========================================================")
    print("Distribución 1 - Esperanza teórica: ", distribucion1Esperanza)
    print("Distribución 1 - Varianza teórica: ", distribucion1Varianza)
    print("Distribución 2 - Esperanza teórica: ", distribucion2Esperanza)
    print("Distribución 2 - Varianza teórica: ", distribucion2Varianza)
    print("Distribución 3 - Esperanza teórica: ", distribucion3Esperanza)
    print("Distribución 3 - Varianza teórica: ", distribucion3Varianza)
    print("==========================================================")
    return

def ejercicio(dist, size):
    if (dist == 1):
        tipoDist = "Binomial"
        distribucion = generarDistribucionBinomial(size)
    elif (dist == 2):
        tipoDist = "Geometrica"
        distribucion = generarDistribucionGeometrica(size)
    elif (dist == 3):
        tipoDist = "Poisson"
        distribucion = generarDistribucionPoisson(size)
    else:
        print("Error: dist debe ser 1, 2 o 3")
        return
    
    media = distribucion.mean()
    mediana = statistics.median(distribucion)
    moda = statistics.mode(distribucion)
    varianza = statistics.variance(distribucion)
    
    plt.boxplot(distribucion)
    plt.title(f"Distribución {tipoDist} - Tamaño: {size}")
    plt.show()

    plt.hist(distribucion, color = 'orange', bins = int(180/5))
    plt.title(f"Distribución {tipoDist} - Tamaño: {size}")
    plt.show()
    
    print("==========================================================")
    print(f"Distribución {tipoDist}, Tamaño: {size}")
    print("Mediana: ", mediana)
    print("Moda: ", moda)
    print("Media empírica de la muestra: ", media)
    print("Varianza empírica de la muestra: ", varianza)
    print("==========================================================")
    return

#====================
#   Variables teóricas
#====================

#variablesTeoricas()

#====================
#   Ejercicio 1
#====================

ejercicio(1,size = 100)
#ejercicio(1,size = 1000)
#ejercicio(1,size = 10000)
#ejercicio(1,size = 100000)


#====================
#   Ejercicio 2
#====================

#ejercicio(2,size = 100)
#ejercicio(2,size = 1000)
#ejercicio(2,size = 10000)
#ejercicio(2,size = 100000)


#====================
#   Ejercicio 3
#====================

#ejercicio(3,size = 100)
#ejercicio(3,size = 1000)
#ejercicio(3,size = 10000)
#ejercicio(3,size = 100000)