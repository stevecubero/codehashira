
# Loggeo a la aplicación 
Nombre = (input ("Ingrese su nombre de usuario:"))
Contraseña = (input ("Ingrese su contraseña:"))

while Nombre and Contraseña:
    if Nombre == "administrador" and Contraseña == "12345":
        print ("Bienvenida/o al registro veterinario")
    else:
        print ("Nombre de usuario o contraseña incorrecto")
        Nombre = (input ("Ingrese nuevamente su nombre de usuario:"))
        Contraseña = (input ("Ingrese nuevamente su contraseña:"))
    break

#Acciones a realizar en el registros de mascotas
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
 

#Acciones a realizar con la ficha clinica
ficha_clinica = (input("¿Desea agregar una nueva ficha clinica si/no?"))

if ficha_clinica == "si":
    modulo = (input("¿En qué modulo desea agregar la ficha? cita/vacuna"))
    if modulo == "cita":
        fecha =(input("Ingrese la fecha que desea agendar la cita"))
        horario =(input("¿A que hora desea que sea la cita"))
        medico = (input("Ingrese el nombre del médico"))
        especialidad =(input("Anote la especilidad requerida"))
        print ("Los datos se ingresaron de la siguiente manera:""\nFecha agendada:", fecha, "a las", horario, "\nMédico:", medico, "\nEspecialidad", especialidad)
    else: 
        medicamento = (input ("Ingrese el medicamento a aplicar"))
        fecha_vacuna = (input("Anote la fecha de vacunación"))
        dosis = (input ("¿Cúal fue la dosis aplicada?"))
        proxima_dosis = (input("Agende la cita de la proxima vacuna"))
    print ("Los datos se ingresaron de la siguiente manera:""\nMedicamento:", medicamento, "\nFecha de la vacuna:", fecha_vacuna, "\nDosis:", dosis, "\nPróxima dosis:", proxima_dosis)
    print ("La ficha clinica se ingreso correctamente")

producto =(input("¿Desea agregar una compra de productos? si/no"))
lista_productos = ("Productos en disponibilidad:" "\nAgrogenta" "\nBiosporine" "\nAgrosona" "\nAgromicyn" "\nAmoxigentil")
precio = 0  
conteo_productos = 0
for x in lista_productos:
    if (x == " "):
        conteo_productos = (conteo_productos + 1)
if producto == "si":
    print (lista_productos)
    condicion = " "
    while condicion != "no":
        condicion = (input ("¿Desea agregar otro producto a su factura? Si su respuesta es sí, ingrese el nombre del medicamento"))
        if condicion == "Agrogenta": 
            precio += 2300 
        elif condicion == "Biosporine":
            precio += 5800
        elif condicion == "Agrosona":
            precio += 3750
        elif condicion == "Agromicyn":
            precio += 7600
        elif condicion == "Amoxigentil":
            precio += 10900
        else: 
            print ("El producto no se encuentra disponible en este momento")
            break
    nombre_cliente = (input("Ingrese el nombre del cliente"))
    descripcion = (input("Ingrese una descripcion de los productos adquiridos"))
    cantidad = int(input("Ingrese la cantidad de productos que adquirio el cliente"))
    subtotal = (cantidad * precio)
    descuento = int (input("Ingrese el descuento en colones a aplicar en la compra"))
    iva = 1.13 
    total_general = ((subtotal - descuento)* iva)
    print ("El total a pagar es de:", total_general)

else: 
    print ("Gracias por su visita")

#Historial 
historial = (input("¿Desea ver el historial?Si/No"))

while historial == "si":
    print ("El total de productos disponible es de:", conteo_productos)
    break

