#Realice un programa que dependiendo del rango de edad y el sexo, retorne un saludo adecuado

#ENTRADAS: EDAD, SEXO
#SALIDAS: saludo adecuado

#PROCESO
#De o a 12 :niñx
#de 13 a 18: adolecente
#de 18 a 24 : joven
#de 25 a 59 :señor
#de 60 en adelante :abuelito

edad = int(input("Digite su edad, por favor:"))
sexo = int (input("Digite 1 si es hombre o 2 si es mujer"))

Saludo =("")

if ( edad <=12 and edad >=0 and sexo==1):
    Saludo = ("niño")
elif (edad <=12 and edad >=0 and sexo==2) :
        Saludo = ("niña")
elif(edad<=18 and edad>=13 and sexo==1):
    Saludo("Querido adolecente")
elif (edad<=18 and edad>=13 and sexo==2):
    Saludo("Querida adolecente")
print("Buen dia",Saludo)

#Version 2
if(sexo==1):
    if(edad<=12 and edad>=0):
        saludo ("niño")
    elif (edad<=18 and edad>=13):
        saludo ("querido adolecente")
    elif (edad<=24 and edad>=19):
        saludo ("querido ajoven")
    elif (edad<=59 and edad>=25):
        saludo ("señor")
    elif (edad>=60):
        saludo ("abuelito")
else:
    saludo("este valor no es valido")

if(sexo==2):
    if(edad<=12 and edad>=0):
        saludo ("niña")
    elif (edad<=18 and edad>=13):
        saludo ("querida adolecente")
    elif (edad<=24 and edad>=19):
        saludo ("querida ajoven")
    elif (edad<=59 and edad>=25):
        saludo ("señora")
    elif (edad>=60):
        saludo ("abuelita")
else:
    saludo("este valor no es valido")
