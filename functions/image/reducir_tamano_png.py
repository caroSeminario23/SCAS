from PIL import Image

from utils.calcular_tamano import calcular_tamano_archivo
from utils.resultado_conversion import resultados_conversion

def reducir_tamano_png(arch_entrada, arch_salida, porcentaje_reduccion):
    print("\nIniciando reducción de tamaño de PNG...")

    # Abrir imagen
    with Image.open(arch_entrada) as img:
        ancho, alto = img.size
        print(f"Tamaño original: {ancho}x{alto}px")

        # Redimensionar la imagen
        if porcentaje_reduccion <= 0 or porcentaje_reduccion > 100:
            raise ValueError("El porcentaje de reducción debe estar entre 1 y 100.")
        
        max_ancho = int(ancho * (porcentaje_reduccion / 100))
        max_alto = int(alto * (porcentaje_reduccion / 100))

        img.thumbnail((max_ancho or ancho, max_alto or alto))
        print(f"Redimensionado a: {img.size[0]}x{img.size[1]}px")

        # Guardar con compresión optimizada
        img.save(
            arch_salida,
            optimize=True,   # Aplica compresión sin pérdida
            quality=80, # Compresión moderada
            format="PNG"
        )

    # Mostrar tamaño antes y después
    tamano_entrada = calcular_tamano_archivo(arch_entrada)
    tamano_salida = calcular_tamano_archivo(arch_salida)

    print("\nReducción completada.")
    return resultados_conversion(arch_entrada, arch_salida, tamano_entrada, tamano_salida)