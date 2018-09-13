##Indique al usuario si ya puede acceder a su pension de vejez

#ENTRADAS: edad, sexo, semanas cotizadas, nombre
#SALIDAS: mensaje

#PROCESO:
#si es hombre mayor de 61 años con 1300 semanas cotizadas podra acceder a su pension
#si es mujer, la misma cantidad de semanas cotizadas pero debe ser mayor a 57 años

nombre = input("Digite su nombre:")
print("vammos a ver si ya puede acceder a su pension", nombre)
edad = int(input("Digite su edad:"))
sexo = int(input("Digite 1 si es hombre o 2 si es mujer:"))
semanasC = int(input("Ingrese la totalidad de semanas cotizadas:"))

if(sexo == 1 and edad>61 and semanasC>=1300 ):
    print("usted puede acceder a su pension")
else:
    if(sexo == 2 and edad>57 and semanasC>1300):
        print("usted puede acceder a su pension")
    else:
        print("Lo sentimos, usted NO puede acceder a su pension")


if(sexo == 1 and edad>61 and semanasC>=1300 ) or (sexo == 2 and edad>57 and semanasC>1300):
    print("usted ya puede acceder a su pension")
else:
    print("lo sentimos, usted no puede acceder a su pension")

    

