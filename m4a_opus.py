import ffmpeg

from utils.calcular_tamano import calcular_tamano_archivo
from utils.resultado_conversion import resultados_conversion

def convertir_m4a_opus(arch_entrada, arch_salida, bitrate="96k"):
    print("\nIniciando conversión de M4A a OPUS...")

    # Tamaño del archivo de entrada en MB
    tamano_entrada = calcular_tamano_archivo(arch_entrada)

    # Conversión del archivo
    (
        ffmpeg
        .input(arch_entrada)
        .output(arch_salida, audio_bitrate=bitrate, acodec="libopus")
        .overwrite_output()
        .run(quiet=True)
    )

    # Tamaño del archivo de salida en MB
    tamano_salida = calcular_tamano_archivo(arch_salida)

    print("\nConversión completada.")
    resultados_conversion(arch_entrada, arch_salida, tamano_entrada, tamano_salida)