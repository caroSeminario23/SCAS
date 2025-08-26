def resultados_conversion(arch_entrada, arch_salida, tamano_entrada, tamano_salida):
    print(f"Archivo de entrada: {arch_entrada} - Peso: {tamano_entrada:.2f} MB")
    print(f"Archivo de salida: {arch_salida} - Peso: {tamano_salida:.2f} MB")
    print(f"Reducción de tamaño: {tamano_entrada - tamano_salida:.2f} MB")