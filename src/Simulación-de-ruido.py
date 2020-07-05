from random import randint, choice

# CONSTANTES PARA EL FUNCIONAMIENTO DEL ARCHIVO
ARCHIVO_ENTRADA = 'codificación-enviada.txt'
ARCHIVO_SALIDA = 'codificación-recibida.txt'

# Originalmente 1%
valor_probabilidad = 0.001

# Se lee el archivo de entrada
archivo_entrada = open(ARCHIVO_ENTRADA, 'r')

# Se obtiene el contenido
data = list(archivo_entrada.read())

archivo_entrada.close()

i =0
while i < len(data):
    # Si el caracter es un 0 o un 1
    # Esto a fin de que solo se alteren los caracteres binarios
    # y no caracteres especiales
    if data[i] in '01' :
        # Se simula si el bit cambia o no
        if randint(0, 100) < valor_probabilidad * 100 :
            # Si la condición se cumple, se sobreescribe el dato
            # con un 0 o 1 aleatorio
            data[i] = choice('01')
    # Se sigue iterando en la data
    i = i + 1

# Se devuelve la data a string
data = ''.join(data)

archivo_salida = open(ARCHIVO_SALIDA, 'w')
archivo_salida.write(data)
archivo_salida.close()
