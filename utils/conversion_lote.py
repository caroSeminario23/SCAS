import os

from utils.porcentaje_reduccion import definir_porcentaje_reduccion
from functions.audio.m4a_mp3 import convertir_m4a_mp3
from functions.audio.m4a_opus import convertir_m4a_opus
from functions.video.mp4_mp3 import convertir_mp4_mp3
from functions.video.mp4opus_mp4mp3 import convertir_m4aopus_mp4mp3
from functions.image.convertir_png_webp import convertir_png_webp
from functions.video.dividir_video import dividir_video_por_tamano
from functions.video.reducir_tamano_mp4 import reducir_tamano_mp4
from functions.image.convertir_png_webp import convertir_png_webp
from functions.image.reducir_tamano_png import reducir_tamano_png

def conversion_por_lote(opcion):
    # Solicitar carpeta de entrada
    carpeta_entrada = input("\nIngrese la ruta de la carpeta: ").strip().strip('"')

    # Validar carpeta de entrada
    if not os.path.isdir(carpeta_entrada):
        raise FileNotFoundError(f"No se encontró la carpeta: {carpeta_entrada}")
    
    # Crear carpeta de salida (nombre_carpeta_entrada + "_2")
    nombre_base = os.path.basename(carpeta_entrada)
    carpeta_salida = os.path.join(os.path.dirname(carpeta_entrada), nombre_base + "_2")
    
    # Crear la carpeta de salida si no existe
    os.makedirs(carpeta_salida, exist_ok=True)
    print(f"\nLos archivos procesados se guardarán en: {carpeta_salida}")

    # Preparar variables para seguimiento
    archivos_procesados = 0
    archivos_con_error = 0
    
    # Determinar extensión de archivo según la opción
    extensiones_entrada = {
        1: ".m4a", 2: ".m4a",  # Audio M4A
        3: ".mp4", 4: ".mp4", 5: ".mp4", 6: ".mp4",  # Video MP4
        7: ".png", 8: ".png"   # Imagen PNG
    }

    extensiones_salida = {
        1: ".opus", 2: ".mp3",  # Audio conversiones
        3: ".mp4", 4: ".mp3", 5: ".mp4", 6: ".mp4",  # Video conversiones
        7: ".webp", 8: ".png"   # Imagen conversiones
    }

    # Comprobar que hay archivos con la extensión correcta
    archivos_a_procesar = [archivo for archivo in os.listdir(carpeta_entrada) 
                          if archivo.endswith(extensiones_entrada.get(opcion, ""))]
    
    if not archivos_a_procesar:
        print(f"\nNo se encontraron archivos con extensión {extensiones_entrada.get(opcion, '')} en la carpeta.")
        return
    
    # Para la opción 8 (reducir PNG), solicitar el porcentaje una sola vez
    porcentaje_reduccion = None
    if opcion == 8:
        porcentaje_reduccion = definir_porcentaje_reduccion()

    print(f"\nSe procesarán {len(archivos_a_procesar)} archivos.")

    # Procesar cada archivo en la carpeta
    for indice, archivo in enumerate(archivos_a_procesar, 1):
        print(f"\n[{indice}/{len(archivos_a_procesar)}] Procesando: {archivo}")

        try:
            # Rutas de entrada y salida
            ruta_entrada = os.path.join(carpeta_entrada, archivo)
            nombre_archivo = os.path.splitext(archivo)[0]
            ext_salida = extensiones_salida.get(opcion, extensiones_entrada.get(opcion, ""))

            # Para todas las opciones excepto la 5 (dividir video)
            if opcion != 5:
                ruta_salida = os.path.join(carpeta_salida, nombre_archivo + ext_salida)
            
            # Llamar a la función correspondiente según la opción
            if opcion == 1:  # M4A a OPUS
                convertir_m4a_opus(ruta_entrada, ruta_salida)
            elif opcion == 2:  # M4A a MP3
                convertir_m4a_mp3(ruta_entrada, ruta_salida)
            elif opcion == 3: # MP4(OPUS) a MP4(MP3)
                convertir_m4aopus_mp4mp3(ruta_entrada, ruta_salida)
            elif opcion == 4:  # MP4 a MP3
                convertir_mp4_mp3(ruta_entrada, ruta_salida)
            elif opcion == 5:  # Dividir video MP4 por tamaño
                carpeta_partes = os.path.join(carpeta_salida, nombre_archivo + "_partes")
                os.makedirs(carpeta_partes, exist_ok=True)
                dividir_video_por_tamano(ruta_entrada, carpeta_partes)
            elif opcion == 6:  # Reducir tamaño de video MP4
                reducir_tamano_mp4(ruta_entrada, ruta_salida)
            elif opcion == 7:  # PNG a WEBP
                convertir_png_webp(ruta_entrada, ruta_salida)
            elif opcion == 8:  # Reducir tamaño de imagen PNG
                reducir_tamano_png(ruta_entrada, ruta_salida, porcentaje_reduccion)
            
            archivos_procesados += 1
            print(f"Archivo procesado correctamente: {archivo}")

        except Exception as e:
            archivos_con_error += 1
            print(f"Error al procesar {archivo}: {e}")


    # Resumen de procesamiento
    print("\n======================")
    print(f"Resumen de procesamiento:")
    print(f"Archivos procesados correctamente: {archivos_procesados}")
    print(f"Archivos con error: {archivos_con_error}")
    print(f"Los resultados están en: {carpeta_salida}")
    print("======================")