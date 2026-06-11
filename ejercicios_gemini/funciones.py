

def registrar_alimento(bitacora_diaria) :

    nombre = input("Ingrese el nombre del alimento : ")

    if nombre == " " :
        print("El nombre no puede estar vacío. ")
        return
    
    if nombre in bitacora_diaria :
        print("El nombre del alimento ya está registrado. ")
        return
    
    try: 
        kilocalorias = float(input("Ingrese el número de kcal : "))

        if kilocalorias < 0 : 
            print("El número debe ser mayor a 0. ")
            return
    except ValueError :
        print("Error. Debe ingresar un número.")
        return

    try: 
        proteina = float(input("Ingrese los gramos de proteina : "))

        if proteina < 0 :
            print("El gramaje de proteína debe ser mayor a 0. ")
            return
        
    except ValueError :
        print("Error. Debe ingresar un número.")
        return
    
#___________________________________________________

def ver_bitacora(bitacora_diaria) :

    if len(bitacora_diaria) == 0 : 
        print("No hay alimentos registrados.")
        return
    
#______________________________________________________

def buscar_alimento(bitacora_diaria) :

    if len(bitacora_diaria) == 0 : 
        print("No hay alimentos registrados. ")
        return

    nombre = input("Ingrese el nombre del alimento : ")

    if nombre not in bitacora_diaria : 
        print("Alimento no encontrado. ")
        return
    
    if nombre in bitacora_diaria :
        datos = bitacora_diaria[nombre]
        print(f"Encontrado! -> kcal: {datos[0]} | proteína: {datos[1]}g")
        