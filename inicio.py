import sys

from utils.convertir_entrada import convertir_entrada
from utils.limpiar_pantalla import limpiar_pantalla
from m4a_mp3 import convertir_m4a_mp3
from m4a_opus import convertir_m4a_opus
from mp4_mp3 import convertir_mp4_mp3
from mp4opus_mp4mp3 import convertir_m4aopus_mp4mp3
from dividir_video import dividir_video_por_tamano

def contenidoMenu():
    print("\nMENU DE OPCIONES")
    print("=================")
    print("1. Convertir M4A a OPUS")
    print("2. Convertir M4A a MP3")
    print("3. Convertir MP4(OPUS) a MP4(MP3)")
    print("4. Convertir MP4 a MP3")
    print("5. Dividir video MP4 por tamaño (200MB)")
    print("6. Salir")


def menu():
    while True:
        contenidoMenu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ruta_entrada, ruta_salida = convertir_entrada("m4a", "opus")
            convertir_m4a_opus(ruta_entrada, ruta_salida)
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

        elif opcion == "2":
            ruta_entrada, ruta_salida = convertir_entrada("m4a", "mp3")
            convertir_m4a_mp3(ruta_entrada, ruta_salida)
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()
        
        elif opcion == "3":
            ruta_entrada, ruta_salida = convertir_entrada("mp4", "mp4")
            convertir_m4aopus_mp4mp3(ruta_entrada, ruta_salida)
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

        elif opcion == "4":
            ruta_entrada, ruta_salida = convertir_entrada("mp4", "mp3")
            convertir_mp4_mp3(ruta_entrada, ruta_salida)
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()
        
        elif opcion == "5":
            ruta_entrada, ruta_salida = convertir_entrada("mp4", "carpeta")
            dividir_video_por_tamano(ruta_entrada, ruta_salida)
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

        elif opcion == "6":
            print("Saliendo...")
            sys.exit()

        else:
            print("Opción no válida. Intente de nuevo.")
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()


# Punto de partida del programa
if __name__ == "__main__":
    print("\nBIENVENIDO AL SISTEMA DE CONVERSIÓN DE AUDIOS Y SECUENCIAS (SCAS) (❁´◡`❁)")
    print("===========================================================================")
    menu()