

usuarios = {}

#______________________funciones__________________________

def ingresar_usuario():

    while True :
        nombre = input("Ingrese nombre de usuario :")

        if nombre in usuarios :
            print("Usuario ya existe. ")
        else: 
            break
    
    while True:
        sexo = input("Ingrese sexo (M, F): ").upper()

        if sexo == "M" or sexo == "F" :
            break
        else:
            print("El sexo debe ser M o F.")

    while True:
        contraseña = input("Ingrese su contraseña:  ")

        if validar_contraseña(contraseña) :
            print("Contraseña válida")
            break

        else:
            print("Contraseña inválida")

    #append es para las listas

    usuarios[nombre] = {                 #aquí se agrega el usuario con diccionarios
        "sexo" : sexo,                   # formato json
        "contraseña" : contraseña
    }



def validar_contraseña(contraseña) :
    if len(contraseña) < 8 :
        return False
    
    if " " in contraseña :
        return False
    
    num = False
    letra = False
    
    for caracter in contraseña :
        if caracter.isdigit() :
            num = True
        
        if caracter.isalpha() :
            letra = True
    
    return num and letra 



def buscar_usuario() :
    nombre = input("Ingrese nombre a buscar: ")

    if nombre in usuarios:
        print("Sexo: ", usuarios[nombre]["sexo"])
        print(f"Contraseña: {usuarios[nombre]["contraseña"]}")

    else:
        print("Nombre no encontrado.")

def eliminar_usuario() :
    nombre = input("Ingrese nombre a eliminar: ")

    if nombre in usuarios :
        del usuarios[nombre]   
        print("Usuario eliminado !")
           
        

#________________menú__________________


while True :
    print("1.- Ingresar usuario")
    print("2.- Buscar usuario")
    print("3.- Eliminar usuario")
    print("4.- Salir")

    while True: 
        try:
            op = int(input("Ingrese la opción: "))
            break
        except ValueError :
            print("Error. Debe ingresar un número.")
        
        


    if op == 1 :
        ingresar_usuario


    elif op == 2 :
        buscar_usuario

    elif op == 3 :
        eliminar_usuario

    elif op == 4 :
        print("Saliendo...")
        break

