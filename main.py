from datos import login  ###IMPORTACIÓN DE FUNCIÓN PARA REUTILIZACIÓN DE ARCHIVOS###
### DICCIONARIO CONTIENE TUPLAS ###
instrumentos = {
    1: ("Acordeón", 10),
    2: ("Bajo", 5),
    3: ("Batería", 3),
    4: ("Guitarra", 15),
    5: ("Piano", 7)
}
### LISTA ###
solicitudes = []
### CONJUNTO ###
clientes = set()

while True:
    print(''' 
    1.- Ingresar solicitud
    2.- Resumen de solicitudes
    3.- Salir
    ''')
    opcion = input("Ingrese una opción:")
    if opcion == "1":
        print(''' 
        *****************************************   
            🎶  INSTRUMENTOS DISPONIBLES 🎵 
        ******************************************  
        ''')  ###  ITERACION ###
        for codigo, instrumento in instrumentos.items():
            nombre, disponibles = instrumento
            print(f"{codigo}.- {nombre} // Disponibles: {disponibles}")

        artefacto = input("\n Seleccione el código del instrumento a reservar," \
        " para finalizar presione 0 :")

        if artefacto == "0":
            print("\n Programa finalizado")
            break
        if not artefacto.isdigit():  ###  CONDICIONALES VALIDACIÓN ###
            print("\n Ingrese sólo números. ⚠")
            continue

        artefacto = int(artefacto)

        if artefacto in instrumentos :
            nombre_instrumento, disponibles = instrumentos[artefacto]

            if disponibles > 0:
                nombre_cliente = input("\n Ingrese el nombre del cliente: ").capitalize()
                solicitudes.append((nombre_cliente, nombre_instrumento))
                clientes.add(nombre_cliente)
                instrumentos[artefacto] =(nombre_instrumento, disponibles -1)
                print(f"\n {nombre_cliente} ha reservado {nombre_instrumento}")

            else:
                print("\n ⛔No quedan disponibles.")
        else:
            print("\n ⚠Instrumento no encontrado.")

    elif opcion == "2":
        print(''' 
            ***********************************************
                🎵🎶 RESUMEN DE SOLICITUDES 🎹🎻🥁🎸
            ***********************************************
        ''')

        if len(solicitudes) == 0:
            print("\n No se han ingresado solicitudes de instrumentos.")
        else:
            print(f"\n Solicitudes ingresadas : {len(solicitudes)}")
            print("LISTA DE SOLICITUDES :")
            for cliente, instrumento in solicitudes:
                print(f"🎼 {cliente} -  🎶 {instrumento}")

        print(f"\n CANTIDAD DE CLIENTES QUE INGRESARON SOLICITUDES :{len(clientes)}")
        print("LISTA DE CLIENTES:")
        for cliente in clientes:
                print(f"  🎼{cliente}")
    elif opcion == "3":
        print(" PROGRAMA FINALIZADO.")
        break
    else:
        print("La opción ingresada no es válida ❌🔇")
