
#funciones

def agregar_producto(productos):
    nombre = input("Ingrese el nombre del producto: ").strip().lower()

    if nombre == "" :
        print("El nombre no puede estar vacío")
        return
    
    if nombre in productos :
        print("Ese producto ya existe.")
        return
    #cuando te dice que TIENE que ser un numero usar try, except.

    try :
        stock = int(input("Ingrese el stock: "))
        if stock < 0 : 
            print("El stock debe ser mayor o igual a 0.")
            return        
    except ValueError :
        print("Error. Debe ingresar un número.")
        return
    
    try:
        precio = float(input("Ingrese el precio : "))
        if precio <= 0 : 
            print("El precio debe ser mayor a 0. ")
            return

    except ValueError :
        print("Error. Precio inválido.")
        return
    
    productos[nombre] = [stock, precio]
    print(f"Producto {nombre} agregado. ")



def mostrar_productos(productos) :

    if len(productos) == 0 :
        print("No hay productos registrados. ")
        return

    for nombre, datos in productos.items():
        print(f"{nombre} | stock: {datos[0]} | precio ${datos[1]}")



def buscar_producto(productos) :
    if len(productos) == 0 : 
        print("No hay productos registrados. ")
        return

    nombre = input("Ingrese el nombre del producto:  ").strip().lower() #te lo devuelve sin espacios, minusculas.

    if nombre in productos :
        datos = productos[nombre]

        print(f"Encontrado! ->  stock: {datos[0]}  |  precio: {datos[1]}")

    else:
        print("Producto no encontrado.")



def producto_mas_caro(productos) :
    if len(productos) == 0 :
        print("No hay productos registrados")
        return

    mayor = 0 
    nombre_mayor = ""

    for nombre in productos : 
        precio = productos [nombre][1]
        if precio > mayor : 
            mayor = precio 
            nombre_mayor = nombre     
    print(f"El producto más caro es {nombre_mayor} con un precio de ${mayor}. ")



    