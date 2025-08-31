import re
import subprocess
from tqdm import tqdm

def ejecutar_conversion(comando_ejecucion, duracion_total):
    # Regex para capturar el tiempo procesado
    regex = re.compile(r"time=(\d+):(\d+):(\d+).(\d+)")

    # Ejecutar proceso
    proceso = subprocess.Popen(comando_ejecucion, stderr=subprocess.PIPE, universal_newlines=True)

    with tqdm(total=duracion_total, unit="s", desc="Convirtiendo", ncols=80) as pbar:
        for linea in proceso.stderr:
            match = regex.search(linea)
            if match:
                h, m, s, ms = match.groups()
                segundos = int(h) * 3600 + int(m) * 60 + int(s)
                pbar.n = segundos
                pbar.refresh()

    proceso.wait()