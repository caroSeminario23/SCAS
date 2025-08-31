import ffmpeg

from utils.ejecutar_conversion import ejecutar_conversion
from utils.obtener_duracion import obtener_duracion
from utils.calcular_tamano import calcular_tamano_archivo
from utils.resultado_conversion import resultados_conversion

def convertir_m4aopus_mp4mp3(arch_entrada, arch_salida, bitrate="96k", crf=28, preset="veryfast"):
    print("\nIniciando conversión de MP4(OPUS) a MP4(MP3)...")

    # Tamaño del archivo de entrada en MB
    tamano_entrada = calcular_tamano_archivo(arch_entrada)

    # Obtener duración total
    duracion_total = obtener_duracion(arch_entrada)

    # Conversión del archivo
    comando_ejecucion = [
        "ffmpeg",
        "-i", arch_entrada, #input
        "-b:a", bitrate, #audio_bitrate
        "-acodec", "libmp3lame",
        '-c:v', 'libx264',
        '-crf', crf,
        '-preset', preset,
        "-y", arch_salida #overwrite output
    ]

    # Ejecución del proceso
    ejecutar_conversion(comando_ejecucion, duracion_total)

    # Tamaño del archivo de salida en MB
    tamano_salida = calcular_tamano_archivo(arch_salida)

    print("\nConversión completada.")
    resultados_conversion(arch_entrada, arch_salida, tamano_entrada, tamano_salida)