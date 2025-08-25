import os
import ffmpeg

def convertir_m4a_opus(arch_entrada, arch_salida, bitrate="96k"):
    print("Iniciando conversión de M4A a OPUS...")

    # Tamaño del archivo de entrada en MB
    tamano_entrada = os.path.getsize(arch_entrada) / (1024*1024)

    # Conversión del archivo
    (
        ffmpeg
        .input(arch_entrada)
        .output(arch_salida, audio_bitrate=bitrate, acodec="libopus")
        .overwrite_output()
        .run(quiet=True)
    )

    # Tamaño del archivo de salida en MB
    tamano_salida = os.path.getsize(arch_salida) / (1024*1024)

    print("Conversión completada.")
    print(f"Archivo de entrada: {arch_entrada} - Peso: {tamano_entrada:.2f} MB")
    print(f"Archivo de salida: {arch_salida} - Peso: {tamano_salida:.2f} MB")