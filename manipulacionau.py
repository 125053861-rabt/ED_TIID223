
print("--- EJERCICIO 1 ---")
calificaciones = [70, 85, 90, 65]
calificaciones.append(95)

calificaciones.insert(2, 80)
print("Arreglo de calificaciones final:", calificaciones)
print()



print("--- EJERCICIO 2 ---")
colores = ["Azul", "Amarillo", "Rosa"]
colores.extend(["Verde", "Morado", "Rojo"])
print("Arreglo completo de colores:", colores)
colores.append("Negro")
print("Color impreso individualmente:", colores[-1])
print()



print("--- EJERCICIO 3 ---")
numeros = [10, 20, 30, 40]
numeros.insert(2, 95)
numeros.extend([50, 67])
print("Arreglo resultante:", numeros)
print("Impresión del 95:", numeros[2])
print("Impresión del 67:", numeros[6])
print("Posición (índice) que ocupa el 95:", numeros.index(95))
print("Posición (índice) que ocupa el 67:", numeros.index(67))