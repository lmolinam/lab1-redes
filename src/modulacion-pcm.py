import numpy as np
import struct
import sys
import wave

from os.path import dirname, join, abspath

PATH_WAV = join(dirname(dirname(abspath(__file__))), "wav", "input")
PATH_TXT = join(dirname(dirname(abspath(__file__))), "txt")
ARCHIVO_SALIDA = 'codificación-enviada.txt'

def obtener_muestras_wav(nombre_wav):
    with wave.open(join(PATH_WAV, nombre_wav), 'r') as wav_entrada:
        frames = wav_entrada.getnframes()
        data = wav_entrada.readframes(frames)
        data = struct.unpack('{n}h'.format(n=frames), data)
    return data

def discretizar_muestras(muestras_wav):
    return [int(muestra) for muestra in muestras_wav]

def digitalizar_muestras(muestras_disc):
    return [np.binary_repr(muestra) for muestra in muestras_disc]

def escribir_codificacion(muestras_dig):
    with open(join(PATH_TXT, ARCHIVO_SALIDA), 'w') as txt_file:
        txt_file.write(repr(muestras_dig))


# en caso de no pasar nombre como parametro se toma nombre default 'entrada.wav'
if len(sys.argv) < 2:
    print("Debe escribir nombre de wav utilizado como input como argumento")
    print("ej: python src/demodulacion-pcm.py shower_2.wav")
    exit(1);
else:
    nombre_wav = sys.argv[1]


# Ejecuta Modulación
muestreo = obtener_muestras_wav(nombre_wav)
muestreo_discretizado = discretizar_muestras(muestreo)
muestreo_digitalizado = digitalizar_muestras(muestreo_discretizado)
escribir_codificacion(muestreo_digitalizado)