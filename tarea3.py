nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi",
            "Teller", "Einstein", "Pele", "Juanes"]

magos = []
cientificos = []
otros = []

for nombre in nombres: 
    if nombre in ["Harry Houdini", "David Blaine", "Teller"]:
        magos.append(nombre)
    elif nombre in ["Newton", "Hawking", "Einstein"]:
        cientificos.append(nombre)
    else:
        otros.append(nombre)

def hacer_grandioso():
    for contador in range (len(magos)):
        magos[contador] = "El gran " + magos[contador]

def imprimir_nombres():
    for nombre in nombres:
        print(nombre)

print("Utilizando función hacer grandioso")
hacer_grandioso()

print("Utilizando función imprimir nombres")
imprimir_nombres()

print("Primer requerimiento, todos los nombres")
for nombre in nombres:
    print(nombre)

print("Segundo requerimiento, lista modificados")
for nombre in magos:
    print(nombre)

print("Tercer requerimiento, lista de científicos")
for nombre in cientificos:
    print(nombre)

print("Cuarto requerimiento, listar los otros nombres")
for nombre in otros:
    print(nombre)