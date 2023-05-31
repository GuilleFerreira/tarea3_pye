from scipy.stats import binom
from scipy.stats import geom
from scipy.stats import poisson
import statistics
import matplotlib.pyplot as plt

# Distribución 1: binomial de parámetros n = 100, p = 0,35.
def generarDistribucion1(size):
    return binom.rvs(100,0.35,size = size)

#Distribución 2: geométrica de parámetro p = 0,08
def generarDistribucion2(size):
    return geom.rvs(0.08,size = size)

#Distribución 3: poisson de parámetro λ = 30.
def generarDistribucion3(size):
    return poisson.rvs(30,size = size)

#Variables
distribucion1 = generarDistribucion1(1000)
distribucion2 = generarDistribucion2(1000)
distribucion3 = generarDistribucion3(1000)


def ejercicio1(size):
    distribucion = generarDistribucion1(1000)
    media = distribucion.mean()
    mediana = statistics.median(distribucion)
    moda = statistics.mode(distribucion)
    varianza = statistics.variance(distribucion)
    
    plt.boxplot(distribucion)
    plt.show()

    plt.hist(distribucion, color = 'orange', bins = int(180/5))
    plt.show()
    
    print("=============================")
    print("Tamaño:", size)
    print("Mediana: ", mediana)
    print("Moda: ", moda)
    print("\n")
    print("Media empírica de la muestra: ", media)
    print("Esperanza teórica de la distribución:")
    print("\n")
    print("Varianza empírica de la muestra: ", varianza)
    print("Varianza teórica de la distribución:")
    print("=============================")
    
    
#====================
#   Ejercicio 1
#====================

#ejercicio1(size = 100)
#ejercicio1(size = 1000)
#ejercicio1(size = 10000)
#ejercicio1(size = 100000)


#====================
#   Ejercicio 2
#====================

#ejercicio2(size = 100)
#ejercicio2(size = 1000)
#ejercicio2(size = 10000)
#ejercicio2(size = 100000)


#====================
#   Ejercicio 3
#====================

#ejercicio3(size = 100)
#ejercicio3(size = 1000)
#ejercicio3(size = 10000)
#ejercicio3(size = 100000)