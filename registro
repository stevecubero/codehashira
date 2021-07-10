
def menuPrincipal ():
    seleccionModulo = int (input ("Selecione el numero del modulo que quiere acceder: 1.Registro 2.Ficha Clinica 3.Producto 4.Historial = "))

    if seleccionModulo == 1:
        registrar ()


def registrar (): 
    registro = (input("¿Desea agregar un nuevo registro? si/no"))
    if registro == "si":
        nombre_usuario = (input("Ingrese el nombre completo del dueño/a de la mascota a registrar:"))
        cedula = (input("Ingrese el numero de cédula:"))
        telefono = (input("Ingrese el número de telefono:"))
        correo = (input("Ingrese un correo:"))
        direccion = (input("Ingrese la dirección de domicilio:"))
        print ("El registro del dueño se ha guardado correctamente")
        nombre_mascota = (input("Ingrese el nombre de la mascota:"))
        raza = (input("¿Cúal es la raza?"))
        nacimiento = (input("¿Cúal es la fecha de nacmiento de la mascota?"))
        sexo = (input ("Ingrese el sexo de la mascota"))
        peso = (input ("indique el peso expresado en gramos"))
        caracteristicas = (input ("Favor indicar algunas caracteristicas de la mascota"))
        alimento = (input ("¿Que marca de alimento come?"))
        observaciones = (input ("De ser necesario favor indique observaciones"))
        print ("El registro se completo de la siguiente manera:")
        print ("Nombre del dueño:", nombre_usuario, "\nCédula:", cedula, "\nTeléfono", telefono, "\ncorreo", correo, "\ndirección", direccion, "\nDatos de la mascota:" 
    "\nNombre de la mascota", nombre_mascota, "\nRaza:", raza, "\nFecha de Nacimiento", nacimiento, "\nSexo", sexo, "\nPeso en Kilos:", peso, "\nCaracteristicas fisicas:", caracteristicas,
    "\nAlimento:", alimento, "\nObservaciones:", observaciones)


# Loggeo a la aplicación 
Nombre = (input ("Ingrese su nombre de usuario:"))
Contraseña = (input ("Ingrese su contraseña:"))

while Nombre and Contraseña:
    if Nombre == "administrador" and Contraseña == "12345":
        print ("Bienvenida/o al sistema veterinario")
        break #cambiar el break en la seccion de logueo del main code
    else:
        print ("Nombre de usuario o contraseña incorrecto")
        Nombre = (input ("Ingrese nuevamente su nombre de usuario:"))
        Contraseña = (input ("Ingrese nuevamente su contraseña:"))
    

menuPrincipal() 

