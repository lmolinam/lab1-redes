import struct
import sys
import wave
import matplotlib.pyplot as plt


from collections import namedtuple
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

def crear_wav(nombre_wav, muestras_reconstruidas, metadata_wav):
    nframes = metadata_wav.nframes
    framerate = metadata_wav.framerate
    comptype = metadata_wav.comptype
    compname = metadata_wav.compname
    nchannels = metadata_wav.nchannels
    sampwidth = metadata_wav.sampwidth
    
    with wave.open(join(PATH_WAV_OUT, nombre_wav), 'w') as wav_salida: 
        wav_salida.setparams((nchannels, sampwidth, int(framerate), nframes, comptype, compname))

        # Se escribe cada muestra de la onda3 en el archivo de salida
        for muestra in muestras_reconstruidas :
            wav_salida.writeframes(struct.pack('h', muestra))


def plotear_wav(nombre_wav):
    with wave.open(join(PATH_WAV_OUT, nombre_wav), 'r') as wav_entrada:
        frames = wav_entrada.getnframes()
        data = wav_entrada.readframes(frames)
        data = struct.unpack('{n}h'.format(n=frames), data)
    
    muestras_discretizadas = [int(muestra) for muestra in data]
    plt.plot(muestras_discretizadas, label='Muestras discretizadas wav generado')
    plt.title('Señal wav generado')
    plt.legend()
    #plt.savefig("señal_recibida.png")
    plt.show()

# en caso de no pasar nombre como parametro se toma nombre default 'salida.wav'
if len(sys.argv) < 2:
    print("Tomando valores default para metadata de wav a crear")
    MetadataWav = namedtuple("MetadataWav", "framerate nframes comptype compname nchannels sampwidth")
    # nframes applause.wav = 400976
    metadata_wav = MetadataWav(48000, 0, "NONE", "not compressed", 1, 2)
else:
    print("Tomando valores de wav original para metadata de wav")
    nombre_wav_original = sys.argv[1]
    metadata_wav = obtener_metadata_wav_original(nombre_wav_original)

if len(sys.argv) < 3:
    nombre_wav_salida = " salida.wav"
else:
    nombre_wav_salida = sys.argv[2]

# Ejecuta Demodulación
muestras_digitales = leer_codificacion_recibida()
muestras_reconstruidas = reconstruir_muestras(muestras_digitales)
print(metadata_wav)
crear_wav(nombre_wav_salida, muestras_reconstruidas, metadata_wav)
#plotear_wav(nombre_wav_salida)





