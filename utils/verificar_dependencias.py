import subprocess

def verificar_dependencias():
    try:
        subprocess.run(["ffmpeg", "-version"], 
                       stdout=subprocess.DEVNULL, 
                       stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        print("Error: FFmpeg no está instalado o no se encuentra en el PATH")
        return False