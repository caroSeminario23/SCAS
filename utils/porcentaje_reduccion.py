def verificar_numero(porcentaje_reduccion):
    if not porcentaje_reduccion.isdigit():
        print("Porcentaje inválido. Debe ser un número entre 1 y 100.")
        return False
    
    porcentaje = int(porcentaje_reduccion)
    if porcentaje < 1 or porcentaje > 100:
        print("Porcentaje inválido. Debe estar entre 1 y 100.")
        return False

    return True


def definir_porcentaje_reduccion():
    porcentaje_reduccion = input("Ingrese el porcentaje de reducción (1-100): ")
    validador = verificar_numero(porcentaje_reduccion)
    while not validador:
        porcentaje_reduccion = input("Ingrese el porcentaje de reducción (1-100): ")
        validador = verificar_numero(porcentaje_reduccion)
    return int(porcentaje_reduccion)