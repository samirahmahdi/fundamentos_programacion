
import funciones as fn

productos = {} #diccionario vacío

while True:
    print("----- MENU -----")
    print("1. Agregar producto")
    print("2. Mostrar Productos")
    print("3. Buscar Productos")
    print("4. Producto más caro")
    print("5. Salir")

    try: 
        op = int(input("Ingrese una opción del menú: "))
    
    except ValueError :
        print("Error. Debe ingresar un número.")
        continue
    

    if op == 1 : 
        fn.agregar_producto(productos)
    
    elif op == 2:
        fn.mostrar_productos(productos) 

    elif op == 3 :
        fn.buscar_producto(productos)
        
    elif op == 4 :
        fn.producto_mas_caro(productos)
    
    elif op == 5 :
        print("Saliendo...")
        break

    else : 
        print("Debe ingresar una opción válida")


    