import subprocess
import os
import math

def dividir_video_por_tamano(archivo_entrada, carpeta_salida, tamano_max_mb=200):
    """
    Divide un video en partes que no superen el tamaño especificado (MB).
    """
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    # Obtener duración total
    cmd_duracion = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", archivo_entrada
    ]
    duracion_total = float(subprocess.check_output(cmd_duracion, text=True).strip())

    # Tamaño total del archivo en MB
    tamano_total = os.path.getsize(archivo_entrada) / (1024 * 1024)
    num_partes = math.ceil(tamano_total / tamano_max_mb)
    duracion_parte = duracion_total / num_partes

    print(f"Tamaño total: {tamano_total:.2f} MB | Dividiendo en {num_partes} partes...")

    for i in range(num_partes):
        inicio = i * duracion_parte
        nombre_base = os.path.basename(carpeta_salida)
        if nombre_base.endswith("_partes"):
            nombre_base = nombre_base[:-7]

        salida = os.path.join(carpeta_salida, f"{nombre_base}_parte_{i+1}.mp4")

        cmd_corte = [
            "ffmpeg", "-ss", str(inicio), "-i", archivo_entrada,
            "-t", str(duracion_parte), "-c", "copy", "-y", salida
        ]

        print(f"Creando parte {i+1}/{num_partes}...")
        subprocess.run(cmd_corte, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Parte {i+1} guardada como {salida}")

    print("\nDivisión completada.")
