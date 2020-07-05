import struct
import sys
import wave


ARCHIVO_ENTRADA = 'codificación-recibida.txt'
NUMERO_MUESTRAS = 48000 
TASA_MUESTREO = 48000.0 # cuántas muestras tomo en un segundo
AMPLITUD = 1000

def leer_codificacion_recibida():
    with open(ARCHIVO_ENTRADA, 'r') as txt_file:
        data = txt_file.read()

def reconstruir_muestras(muestras_dig):
    return [int(binario, '2') for binario in muestras_dig]

def crear_wav(nombre_wav, muestras_reconstruidas):
    nframes = NUMERO_MUESTRAS
    comptype = 'NONE' # tipo compresión
    compname = 'not compressed' # nombre compresión
    nchannels = 1 # número de canales
    sampwidth = 2 # ancho de muestras
    
    with wave.open(nombre_wav, 'w') as wav_salida: 
        wav_salida.setparams((nchannels, sampwidth, int(TASA_MUESTREO), nframes, comptype, compname))

        # Se escribe cada muestra de la onda3 en el archivo de salida
        for muestra in muestras_reconstruidas :
            wav_salida.writeframes(struct.pack('h', int(muestra * AMPLITUD)))


# en caso de no pasar nombre como parametro se toma nombre default 'salida.wav'
if len(sys.argv) < 2:
    nombre_wav = " salida.wav"
else:
    nombre_wav = sys.argv[1]

muestras_digitales = leer_codificacion_recibida():
muestras_reconstruidas = reconstruir_muestras(muestras_digitales)
crear_wav(nombre_wav, muestras_reconstruidas)