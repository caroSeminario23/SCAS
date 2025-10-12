def resultados_conversion(arch_entrada, arch_salida, tamano_entrada, tamano_salida):
    print(f"Archivo de entrada: {arch_entrada} - Peso: {tamano_entrada:.2f} MB")
    print(f"Archivo de salida: {arch_salida} - Peso: {tamano_salida:.2f} MB")

    diferencia_tamano = tamano_entrada - tamano_salida
    porcentaje_reduccion = ((tamano_entrada - tamano_salida) / tamano_entrada) * 100
    
    print(f"Reducción de tamaño: {diferencia_tamano:.2f} MB ({porcentaje_reduccion:.1f}%)")