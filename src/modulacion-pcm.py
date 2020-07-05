import numpy as np
import struct
import sys
import wave

ARCHIVO_SALIDA = 'codificación-enviada.txt'

def obtener_muestras_wav(nombre_wav):
    with wave.open(nombre_wav, 'r') as wav_entrada:
        frames = wav_entrada.getnframes()
        data = wav_entrada.readframes(frames)
        data = struct.unpack('{n}h'.format(n=frames), data)
    return data

def discretizar_muestras(muestras_wav):
    return [int(muestra) for muestra in muestras_wav]

def digitalizar_muestras(muestras_disc):
    return [np.binary_repr(muestra) for muestra in muestras_disc]

def escribir_codificacion(muestras_dig):
    with open(ARCHIVO_SALIDA, 'w') as txt_file:
        txt_file.write(muestras_dig)


# en caso de no pasar nombre como parametro se toma nombre default 'entrada.wav'
if len(sys.argv) < 2:
    nombre_wav = " entrada.wav"
else:
    nombre_wav = sys.argv[1]

wav = leer_wav(nombre_wav)
muestreo = muestrear_wav(wav)
muestreo_discretizado = discretizar_muestras(muestreo)
muestreo_digitalizado = digitalizar_muestras(muestreo_discretizado)
escribir_codificacion(muestreo_digitalizado)