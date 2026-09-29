matriz =[
    [1,2,3],
    [4,5,6]
]
print("Mostrar la matriz")
for fila in matriz:
    print(fila)

print("Mostrar el 6")
print(matriz[1][2])


print(matriz[0])

""" Sobreescribiendo valor """
matriz[1][1] = 8

matriz.append([7,8,9])
print(matriz)

matriz[0].pop(2)
print(matriz)