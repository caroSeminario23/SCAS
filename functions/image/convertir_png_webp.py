from PIL import Image

from utils.calcular_tamano import calcular_tamano_archivo
from utils.resultado_conversion import resultados_conversion

def convertir_png_webp(arch_entrada, arch_salida):
    print("\nIniciando conversión de PNG a WEBP...")

    # Abrir y convertir
    with Image.open(arch_entrada) as img:
        img = img.convert("RGBA")  # Asegurar canal alfa si lo tiene
        img.save(arch_salida, "WEBP", quality=80, method=6)

    # Mostrar tamaños antes y después
    tamano_entrada = calcular_tamano_archivo(arch_entrada)
    tamano_salida = calcular_tamano_archivo(arch_salida)

    print("\nConversión completada.")
    return resultados_conversion(arch_entrada, arch_salida, tamano_entrada, tamano_salida)