# lab1-redes

## Instrucciones de uso

### Ejecutar archivo de modulación

Los archivos wav a utilizar deben estar en la carpeta wav/input
Se debe otorgar como parámetro el wav a utilizar en caso de no otorgar parámetro con wav a utilizar se intenta usar por defecto el nombre 'entrada.wav'

- Ejemplo: python src/modulacion-pcm.py shower_2.wav

### Ejecutar arhivo de simulación de ruido

Lee archivo 'codificación-enviada.txt' generado cpn la ejecución previa del script 'modulacion-pcm.py'. Escribe salida en archivo 'codificación-recibida.txt'.

Ambos archivos quedan ubicados en la carpeta 'txt'

- Ejemplo: python src/simulacion-ruido.py

### Ejecutar archivo de demodulación

Se debe otorgar como parámetro el nombre del wav utilizado en el proceso de modulación. Lee el archivo 'codificación-recibida.txt' generado con la ejecución previa del script 'simulacion-ruido.py'.

- Ejemplo: python src/demodulacion-pcm.py shower_2.wav