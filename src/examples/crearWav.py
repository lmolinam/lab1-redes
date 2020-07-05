# -*- coding: cp1252 -*-
# Se importa numpy para usar las funciones sen,
# array y la constante pi
import numpy as np
# Se importa para generar el archivo de audio
import wave
# Se importa struct para empaquetar los valores
# de las muestras en hexadecimal
import struct
# Se utiliza para generar gr�ficos
import matplotlib.pyplot as plt

# Frencuencias 
frecuencia = 19000

frecuencia2 = 20000

# N�mero de muestras tomadas
numeroDeMuestras = 48000 

# Cu�ntas muestras tomo en un segundo
tasaDeMuestreo = 48000.0 

# Amplitud
amplitud = 1000

# Nombre del archivo
salida = 'ejemplo13-05.wav'

# Ecuaciones
# Se genera un vector con el valor
# del la ecuaci�n del seno, para cada muestra
# Se elimina el valor de
# amplitud del c�lculo para a�adir la amplitud a la onda resultante
onda = [np.sin(2 * np.pi * frecuencia * x/tasaDeMuestreo) for x in range(numeroDeMuestras)]

onda2 = [0.5 * np.sin(2 * np.pi * frecuencia2 * x/tasaDeMuestreo) for x in range(numeroDeMuestras)]

# Se suman las dos ondas para generar la se�al compuesta
onda3 = np.array(onda) + np.array(onda2)

'''
onda = []

for x in range(numeroDeMuestras) :
    valor = 2 * np.pi * frecuencia * x/tasaDeMuestreo
    onda.append(valor)
'''

# LINEAS QUE GENERAN EL WAV
# Se declara el n�mero de muestras que se utilizar�n para el wav
nframes = numeroDeMuestras
# Se determina el tipo y nombre de la compresi�n
# el n�mero de canales y el ancho de muestras
comptype = 'NONE'
compname = 'not compressed'
nchannels = 1
sampwidth = 2
# Se abre el archivo en modo de escritura
archivoSalida = wave.open(salida, 'w')
# Se configuran los par�metros del archivo a escribir
archivoSalida.setparams((nchannels, sampwidth, int(tasaDeMuestreo), nframes, comptype, compname))

# Se escribe cada muestra de la onda3 en el archivo de salida
for muestra in onda3 :
    archivoSalida.writeframes(struct.pack('h', int(muestra * amplitud)))
    
# Se cierra el archivo de salida
archivoSalida.close()

# LINEAS QUE GENERAN EL GR�FICO
# Se genera la recta de la primera onda
grafico = plt.plot(onda, label='onda 1')
# Se genera la recta de la segunda onda 
grafico2 = plt.plot(onda2, label='onda 2')
# Se genera el gr�fico de la onda resultante 
grafico3 = plt.plot(onda3, label='onda 3')
# Se agrega un t�tulo al gr�fico 
plt.title('Se�al mostrada')
# Se muestra la leyenda para identificar las ondas 
plt.legend()
# Se muestra el gr�fico por pantalla
plt.show()

