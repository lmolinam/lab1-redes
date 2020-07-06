import struct
import sys
import wave

from os.path import dirname, join, abspath

PATH_WAV_OUT = join(dirname(dirname(abspath(__file__))), "wav", "output")
PATH_WAV_IN = join(dirname(dirname(abspath(__file__))), "wav", "input")
PATH_TXT = join(dirname(dirname(abspath(__file__))), "txt")
ARCHIVO_ENTRADA = 'codificación-recibida.txt'
AMPLITUD = 1000

def obtener_metadata_wav_original(nombre_wav):
    with wave.open(join(PATH_WAV_IN, nombre_wav), 'r') as wav_file:
        return wav_file.getparams()

def leer_codificacion_recibida():
    with open(join(PATH_TXT, ARCHIVO_ENTRADA), 'r') as txt_file:
        data = list(txt_file.read())

    return data

def reconstruir_muestras(muestras_dig):
    aux_binario = ""
    muestras_rec = []
    for caracter in muestras_dig:
        if caracter == "[" or caracter == "]" or caracter == "'":
            continue
        elif caracter != ",":
            aux_binario += caracter
        else:
            muestras_rec.append(int(aux_binario, 2))
            aux_binario = ""

    return muestras_rec

def crear_wav(nombre_wav, muestras_reconstruidas, metadata_orig_wav):
    nframes = metadata_orig_wav.nframes
    framerate = metadata_orig_wav.framerate
    comptype = metadata_orig_wav.comptype
    compname = metadata_orig_wav.compname
    nchannels = metadata_orig_wav.nchannels
    sampwidth = metadata_orig_wav.sampwidth
    
    with wave.open(join(PATH_WAV_OUT, nombre_wav), 'w') as wav_salida: 
        wav_salida.setparams((nchannels, sampwidth, int(framerate), nframes, comptype, compname))

        # Se escribe cada muestra de la onda3 en el archivo de salida
        for muestra in muestras_reconstruidas :
            wav_salida.writeframes(struct.pack('h', muestra))


# en caso de no pasar nombre como parametro se toma nombre default 'salida.wav'
if len(sys.argv) < 2:
    print("Debe escribir nombre de wav utilizado como input como argumento")
    print("ej: python src/demodulacion-pcm.py shower_2.wav")
    exit(1);
else:
    nombre_wav_original = sys.argv[1]

if len(sys.argv) < 3:
    nombre_wav_salida = " salida.wav"
else:
    nombre_wav_salida = sys.argv[2]

# Ejecuta Demodulación
muestras_digitales = leer_codificacion_recibida()
muestras_reconstruidas = reconstruir_muestras(muestras_digitales)
metadata_wav_original = obtener_metadata_wav_original(nombre_wav_original)
crear_wav(nombre_wav_salida, muestras_reconstruidas, metadata_wav_original)