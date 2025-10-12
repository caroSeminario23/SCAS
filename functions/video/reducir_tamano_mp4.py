from utils.ejecutar_conversion import ejecutar_conversion
from utils.obtener_duracion import obtener_duracion
from utils.calcular_tamano import calcular_tamano_archivo
from utils.resultado_conversion import resultados_conversion

def reducir_tamano_mp4(arch_entrada, arch_salida):
    print("\nIniciando reducción de tamaño de MP4...")

    # Tamaño del archivo de entrada en MB
    tamano_entrada = calcular_tamano_archivo(arch_entrada)

    # Obtener duración total
    duracion_total = obtener_duracion(arch_entrada)

    # Conversión del archivo
    comando_ejecucion = [
        "ffmpeg", "-i", arch_entrada,
        "-vf", "scale=1280:-1,fps=30", # Filtros de video combinados
        "-c:v", "libx264",             # Codec de video
        "-crf", "28",                  # Control de calidad (más alto = menos calidad)
        "-preset", "veryfast",         # Velocidad de codificación
        "-b:a", "96k",                 # Bitrate de audio
        "-acodec", "aac",              # Codec de audio
        "-movflags", "faststart",      # Optimización para streaming
        "-y", arch_salida
    ]

    # Ejecución del proceso
    ejecutar_conversion(comando_ejecucion, duracion_total)

    # Tamaño del archivo de salida en MB
    tamano_salida = calcular_tamano_archivo(arch_salida)

    print("\nConversión completada.")
    resultados_conversion(arch_entrada, arch_salida, tamano_entrada, tamano_salida)