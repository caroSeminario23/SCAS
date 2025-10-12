import os

def convertir_entrada(formato_entrada, formato_salida):
    archivo = input(f"\nIngrese la ruta del archivo {formato_entrada} de entrada: ")

    # Validación de entrada
    if not os.path.isfile(archivo):
        raise FileNotFoundError(f"No se encontró el archivo: {archivo}")

    ruta_entrada = os.path.normpath(archivo.strip().strip('"'))

    if formato_salida == "carpeta":
        ruta_carpeta = os.path.splitext(ruta_entrada)[0]
        ruta_salida = os.path.normpath(ruta_carpeta + "_partes")
        os.makedirs(ruta_salida, exist_ok=True)
    else:
        ruta_salida = os.path.splitext(ruta_entrada)[0] + f"_2.{formato_salida}"
        
    return ruta_entrada, ruta_salida


def convertir_entrada_lote(carpeta_entrada, archivo, formato_salida):
    ruta_entrada = os.path.join(carpeta_entrada, archivo)
    ruta_salida = os.path.splitext(ruta_entrada)[0] + f"_2.{formato_salida}"

    return ruta_entrada, ruta_salida