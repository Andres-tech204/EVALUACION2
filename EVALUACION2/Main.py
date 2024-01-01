
compras = []
suma_de_compras = 0

def agregarcompras():
    compra1 = int(input("Ingrese monto de la compra= "))
    compras.append(compra1)
    print("------------------------------------Compra agregada correctamente------------------------------------")

def mostrarcompras():
    for indice, compra in enumerate(compras):
        print(f"Compra numero {indice}: {compra}")

def sumarcompras():
    suma_de_compras = sum(compras)
    print("---------------------------------------- $",suma_de_compras, "-----------------------------------------------")

while True:
    print("1. Agregar compra")
    print("2. Mostrar compra")
    print("3. Mostrar total gastado")
    print("4. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        agregarcompras()
    if opcion == 2:
        mostrarcompras()
    if opcion == 3:
        sumarcompras()
    if opcion == 4:
        print("Bye Bye!!")
        exit()
