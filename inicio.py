import sys

from utils.convertir_entrada import convertir_entrada
from utils.limpiar_pantalla import limpiar_pantalla
from utils.porcentaje_reduccion import definir_porcentaje_reduccion
from utils.conversion_lote import conversion_por_lote
from utils.verificar_dependencias import verificar_dependencias
from functions.audio.m4a_mp3 import convertir_m4a_mp3
from functions.audio.m4a_opus import convertir_m4a_opus
from functions.video.mp4_mp3 import convertir_mp4_mp3
from functions.video.mp4opus_mp4mp3 import convertir_m4aopus_mp4mp3
from functions.video.dividir_video import dividir_video_por_tamano
from functions.video.reducir_tamano_mp4 import reducir_tamano_mp4
from functions.image.convertir_png_webp import convertir_png_webp
from functions.image.reducir_tamano_png import reducir_tamano_png


def contenidoMenuPrincipal():
    print("\nMENÚ PRINCIPAL")
    print("=================")
    print("1. Procesar un archivo")
    print("2. Procesar un lote de archivos")
    print("3. Salir")

def contenidoMenuSecundario():
    limpiar_pantalla()
    print("\nMENU DE OPCIONES")
    print("=================")
    print("AUDIOS")
    print("=================")
    print("1. Convertir M4A a OPUS")
    print("2. Convertir M4A a MP3")
    print("\nVIDEOS")
    print("=================")
    print("3. Convertir MP4(OPUS) a MP4(MP3)")
    print("4. Convertir MP4 a MP3")
    print("5. Dividir video MP4 por tamaño (200MB)")
    print("6. Reducir tamaño de video MP4")
    print("\nIMÁGENES")
    print("=================")
    print("7. Convertir PNG a WEBP")
    print("8. Reducir tamaño de imagen PNG")
    print("\n=================")
    print("9. Regresar al menú principal")
    print("10. Salir")


def menuSecundario(tipo): # 1: individual, 2: lote
    while True:
        contenidoMenuSecundario()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            if tipo == 1:
                ruta_entrada, ruta_salida = convertir_entrada("m4a", "opus")
                try:
                    convertir_m4a_opus(ruta_entrada, ruta_salida)
                except Exception as e:
                    print(f"Error al convertir M4A a OPUS: {e}")
            if tipo == 2:
                conversion_por_lote(1)
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

        elif opcion == "2":
            if tipo == 1:
                ruta_entrada, ruta_salida = convertir_entrada("m4a", "mp3")
                try:
                    convertir_m4a_mp3(ruta_entrada, ruta_salida)
                except Exception as e:
                    print(f"Error al convertir M4A a MP3: {e}")
            if tipo == 2:
                conversion_por_lote(2)
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()
        
        elif opcion == "3":
            if tipo == 1:
                ruta_entrada, ruta_salida = convertir_entrada("mp4", "mp4")
                try:
                    convertir_m4aopus_mp4mp3(ruta_entrada, ruta_salida)
                except Exception as e:
                    print(f"Error al convertir MP4(OPUS) a MP4(MP3): {e}")
            if tipo == 2:
                conversion_por_lote(3)
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

        elif opcion == "4":
            if tipo == 1:
                ruta_entrada, ruta_salida = convertir_entrada("mp4", "mp3")
                try:
                    convertir_mp4_mp3(ruta_entrada, ruta_salida)
                except Exception as e:
                    print(f"Error al convertir MP4 a MP3: {e}")
            if tipo == 2:
                conversion_por_lote(4)
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()
        
        elif opcion == "5":
            if tipo == 1:
                ruta_entrada, ruta_salida = convertir_entrada("mp4", "carpeta")
                try:
                    dividir_video_por_tamano(ruta_entrada, ruta_salida)
                except Exception as e:
                    print(f"Error al dividir video por tamaño: {e}")
            if tipo == 2:
                conversion_por_lote(5)
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

        elif opcion == "6":
            if tipo == 1:
                ruta_entrada, ruta_salida = convertir_entrada("mp4", "mp4")
                try:
                    reducir_tamano_mp4(ruta_entrada, ruta_salida)
                except Exception as e:
                    print(f"Error al reducir tamaño de video MP4: {e}")
            if tipo == 2:
                conversion_por_lote(6)
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

        elif opcion == "7":
            if tipo == 1:
                ruta_entrada, ruta_salida = convertir_entrada("png", "webp")
                try:
                    convertir_png_webp(ruta_entrada, ruta_salida)
                except Exception as e:
                    print(f"Error al convertir PNG a WEBP: {e}")
            if tipo == 2:
                conversion_por_lote(7)
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

        elif opcion == "8":
            if tipo == 1:
                ruta_entrada, ruta_salida = convertir_entrada("png", "png")
                porcentaje_reduccion = definir_porcentaje_reduccion()
                try:
                    reducir_tamano_png(ruta_entrada, ruta_salida, porcentaje_reduccion)
                except Exception as e:
                    print(f"Error al reducir tamaño de PNG: {e}")
            if tipo == 2:
                conversion_por_lote(8)
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

        elif opcion == "9":
            print("Regresando al menú principal...")
            limpiar_pantalla()
            return # Salir de menuSecundario y volver a menuPrincipal

        elif opcion == "10":
            print("Saliendo...")
            sys.exit()

        else:
            print("Opción no válida. Intente de nuevo.")
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

def menuPrincipal():
    while True:
        contenidoMenuPrincipal()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menuSecundario(1)
        elif opcion == "2":
            menuSecundario(2)
        elif opcion == "3":
            print("Saliendo...")
            sys.exit()
        else:
            print("Opción no válida. Intente de nuevo.")
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()


# Punto de partida del programa
if __name__ == "__main__":
    if not verificar_dependencias():
        sys.exit(1)

    print("\nBIENVENIDO AL SISTEMA DE CONVERSIÓN DE AUDIOS Y SECUENCIAS (SCAS) (❁´◡`❁)")
    print("===========================================================================")
    menuPrincipal()