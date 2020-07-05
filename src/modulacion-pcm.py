import numpy as np
import struct
import sys
import wave

ARCHIVO_SALIDA = 'codificación-enviada.txt'

def obtener_muestras_wav(nombre_wav):
    archivo_entrada = wave.open(nombre_wav, 'r')
    frames = archivo_entrada.getnframes()
    data = archivo_entrada.readframes(frames)
    data = struct.unpack('{n}h'.format(n=frames), data)
    archivo_entrada.close()
    return data

def discretizar_muestras(muestras_wav):
    return [int(muestra) for muestra in muestras_wav]

def digitalizar_muestras(muestras_disc):
    return [np.binary_repr(muestra) for muestra in muestras_disc]

def escribir_codificacion(muestras_dig):
    with open(ARCHIVO_SALIDA, 'w') as txt_file:
        txt_file.write(muestras_dig)


# en caso de no pasar nombre como parametro se toma nombre default 'ejemplo.wav'
if len(sys.argv) < 2:
    nombre_archivo = " ejemplo.wav"
else:
    nombreArchivo = sys.argv[1]

wav = leer_wav(nombre_archivo)
muestreo = muestrear_wav(wav)
muestreo_discretizado = discretizar_muestras(muestreo)
muestreo_digitalizado = digitalizar_muestras(muestreo_discretizado)
escribir_codificacion(muestreo_digitalizado)