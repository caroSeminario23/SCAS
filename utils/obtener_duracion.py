import ffmpeg

def obtener_duracion(arch_entrada):
    probe = ffmpeg.probe(arch_entrada)
    duracion_total = float(probe["format"]["duration"])  # en segundos
    return duracion_total