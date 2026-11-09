# Crear algoritmo que pueda organizar 3 variables (x, y, z) de menor a mayor.

x = int(input("Ingrese variable x: "))
y = int(input("Ingrese variable y: "))
z = int(input("Ingrese variable z: "))

# Mayor
if x >= y and x >= z:
    may = x
elif y >= z:
    may = y
else:
    may = z

# Menor
if x <= y and x <= z:
    men = x
elif y <= z:
    men = y
else:
    men = z

# Medio
if (x >= y and x <= z) or (x <= y and x >= z):
    med = x
elif (y >= x and y <= z) or (y <= x and y >= z):
    med = y
else:
    med = z

print(f"Ver resultado ordenado: menor: {men} medio: {med} mayor: {may}")