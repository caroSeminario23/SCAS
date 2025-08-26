import os

def calcular_tamano_archivo(archivo):
    # Calcula el tamaño de un archivo en MB.
    return os.path.getsize(archivo) / (1024 * 1024)