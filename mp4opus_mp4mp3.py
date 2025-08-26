import ffmpeg

from utils.calcular_tamano import calcular_tamano_archivo
from utils.resultado_conversion import resultados_conversion

def convertir_m4aopus_mp4mp3(arch_entrada, arch_salida, bitrate="96k", crf=28, preset="veryfast"):
    print("\nIniciando conversión de MP4(OPUS) a MP4(MP3)...")

    # Tamaño del archivo de entrada en MB
    tamano_entrada = calcular_tamano_archivo(arch_entrada)

    # Conversión del archivo
    try:
        (
            ffmpeg
            .input(arch_entrada)
            .output(
                arch_salida,
                **{
                    'c:v': 'libx264',
                    'crf': crf,
                    'preset': preset,
                    'c:a': 'libmp3lame',
                    'b:a': bitrate
                }
            )
            .overwrite_output()
            .run(quiet=True)
        )
    except ffmpeg.Error as e:
        print("\n[ERROR] ffmpeg stderr:\n")
        print(e.stderr.decode() if e.stderr else "No hay salida de error de ffmpeg.")
        raise

    # Tamaño del archivo de salida en MB
    tamano_salida = calcular_tamano_archivo(arch_salida)

    print("\nConversión completada.")
    resultados_conversion(arch_entrada, arch_salida, tamano_entrada, tamano_salida)