import os

def convertir_entrada(formato):
    archivo = input("\nIngrese la ruta del archivo M4A de entrada: ")
    ruta_entrada = os.path.normpath(archivo.strip().strip('"'))
    ruta_salida = os.path.splitext(ruta_entrada)[0] + f"_2.{formato}"
    return ruta_entrada, ruta_salida