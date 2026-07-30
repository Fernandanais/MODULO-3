def login(user, password):
    usuario = "plantas"
    clave = "123456"
    return user == usuario and password == clave

intentos = 0
max_intentos = 3

while intentos < max_intentos:
    usuario = input("Ingrese nombre de usuario: ")
    clave = input("Ingrese su contreseña: ")

    if login(usuario, clave):
        print(" ✔ Acceso correcto, 🎵🎶¡¡¡Bienvenid@!!! 🎶🎵")
        break

    intentos +=1
    if (intentos < max_intentos):
        print(f" Usuario y/o Contreseña incorrecta, intento {intentos} de {max_intentos}")
else: 
    print(f"Ha alcanzado el máximo número de intentos, cuenta bloqueada.⛔")
    exit()


