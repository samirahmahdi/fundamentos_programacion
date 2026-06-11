
import funciones as fn


bitacora_diaria = {}


while True :
    print("------CALO-TRACK MENU-------")
    print("1.-Registrar alimento")
    print("2.-Ver bitácora diaria")
    print("3.-Buscar alimento consumido")
    print("4.-Calcular totales del día")
    print("5.-Alimento más proteico")
    print("6.-Salir")

    try: 
        op = int(input("Ingrese una opción del menú : "))

    except ValueError :
        print("Error, debe ingresar un número.")

    if op == 1 :
        fn.registrar_alimento(bitacora_diaria)
    
    elif op == 2:
        fn.ver_bitacora(bitacora_diaria)

    elif op == 3 :
        fn.buscar_alimento(bitacora_diaria)

    
    elif op == 6 :
        print("Saliendo...")
        break

    else: 
        print("Ingrese una opción válida del 1 al 6.")
   