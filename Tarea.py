'''
Descripcion programa: 

El departamento Financiero de la empresa XYZ le ha solicitado que le prepare un programa que le permita 
calcular el futuro aumento que se aplicará a los empleados, este aumento consiste de lo siguiente.
El programa recibirá del usuario la cantidad de horas trabajadas al mes y el valor pagado por cada hora, 
con esto calculará el salario bruto , a este salario le aplicará un 4.25 % de incremento de ley; adicionalmente la empresa 
por sus buenos ingresos del año pasado ha considerado otorgar un bono adicional del 1.57 %, ambos sobre el salario bruto.
Una vez calculado el nuevo salario, deberá aplicar los siguientes rebajos.

-	10.14 % por Pago de Caja.
-	3.5 % por pertenecer a la Asociación Solidarista.
-	2 % por pertenecer al Fondo de Ahorro Voluntario de la empresa.
-	8.5 % por el Fondo de Ahorro Navideño.
-	1 % por el Fondo de Ayuda a personas afectadas por la pandemia.

Todas las deducciones presentadas se aplican sobre el nuevo salario calculado.
Finalmente, el programa debe presentar al usuario el desglose del nuevo salario bruto, cada una de las deducciones 
con su descripción y el salario neto o final.

Created by: Steven Cubero Quesada 
'''
#en la siguiente seccion el usuario debe digitar las horas trabajada y el valor de cada hora

horasTrabajadas = int (input("Digite el total de horas laboradas este mes: "))
valorHora = int (input("Digite el valor de cada hora de trabajo: "))

#en la siguiente seccion se calcula el salario total contando bono y aumento

salarioBruto = horasTrabajadas * valorHora 
aumentoSalarial = (salarioBruto * 4.25) / 100 #aumento salario de 4.25%
bonoMensual = (salarioBruto * 1.57) / 100 #bonomensual
salarioTotal = salarioBruto + aumentoSalarial + bonoMensual #nuevo salario contanto aumento y bono

#en la siguiente seccion se calculan las deducciones totales

ccss = (salarioTotal* 10.14) / 100
asociacionSolidarista = (salarioTotal * 3.5) / 100
ahorroVoluntario = (salarioTotal * 2) / 100
ahorroNavideno = (salarioTotal * 8.5) / 100 
ayudaPandemia = (salarioTotal * 1 ) / 100 


#en la siguiente seccion se muestra el desglose salarial y el salario final despues de las deducciones

print("Su salario bruto mensual es: ", salarioTotal)

print("Porcentaje deducido por la CCSS: " ,ccss)
print("Porcentaje deducido por la asociacion solidarista: ", asociacionSolidarista)
print("Porcentaje deducido por ahorro voluntario: ", ahorroVoluntario)
print("Porcentaje deducido por ahorro navideno: ", ahorroNavideno)
print("Porcentaje deducido por ayuda voluntaria a personas afectadas por pandemia: ", ayudaPandemia)

print("Salario final despues de deducciones: ", salarioTotal - ccss - asociacionSolidarista - ahorroVoluntario - ahorroNavideno - ayudaPandemia)

