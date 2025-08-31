import os
from m4a_mp3 import convertir_m4a_mp3
from m4a_opus import convertir_m4a_opus
from mp4_mp3 import convertir_mp4_mp3
from mp4opus_mp4mp3 import convertir_m4aopus_mp4mp3

def convertir_entrada(formato):
    archivo = input("\nIngrese la ruta del archivo M4A de entrada: ")
    ruta_entrada = os.path.normpath(archivo.strip().strip('"'))
    ruta_salida = os.path.splitext(ruta_entrada)[0] + f"_2.{formato}"
    return ruta_entrada, ruta_salida

def menu():
    print("MENU DE OPCIONES")
    print("=================")
    print("1. Convertir M4A a OPUS")
    print("2. Convertir M4A a MP3")
    print("3. Convertir MP4(OPUS) a MP4(MP3)")
    print("4. Convertir MP4 a MP3")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ruta_entrada, ruta_salida = convertir_entrada("opus")
        convertir_m4a_opus(ruta_entrada, ruta_salida)

    elif opcion == "2":
        ruta_entrada, ruta_salida = convertir_entrada("mp3")
        convertir_m4a_mp3(ruta_entrada, ruta_salida)
    
    elif opcion == "3":
        ruta_entrada, ruta_salida = convertir_entrada("mp4")
        convertir_m4aopus_mp4mp3(ruta_entrada, ruta_salida)

    elif opcion == "4":
        ruta_entrada, ruta_salida = convertir_entrada("mp3")
        convertir_mp4_mp3(ruta_entrada, ruta_salida)

    elif opcion == "5":
        print("Saliendo...")
        exit()

    else:
        print("Opción no válida. Intente de nuevo.")


# Punto de partida del programa
if __name__ == "__main__":
    print("\nBIENVENIDO AL SISTEMA DE CONVERSIÓN DE AUDIOS (SCAS)")
    menu()