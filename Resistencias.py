'''Programa: Calculando resistencias.
Objetivo: Calcular cuatro (4) resistencias de un circuito paralelo.
Estudiantes: "mauricio Bohorquez"



#Entrada

res1 = float(input("Resistencia 1: "))
res2 = float(input("Resistencia 2: "))
res3 = float(input("Resistencia 3: "))
res4 = float(input("Resistencia 4: "))



#Proceso

resqui = 1/((1/res1)+(1/res2)+(1/res3)+(1/res4))


#Salida


print("La resistencia equivalente es: ", resqui, "Ohmios")



