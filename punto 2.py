print("*******************ALMACEN: VENTA DE TELEFONOS****************")
print("***************************MARCAS*****************************")
print("CÓDIGO 1: Sony")
print("CÓDIGO 2: Samsung")
print("CÓDIGO 3: Huawei")
print("*****************************PLAN*****************************")
print("CÓDIGO 1: Prepago")
print("CÓDIGO 2: Postpago")
print("**************************************************************")

z= 0
w= 0
y= 0

n=int(input("Numero de telefonos: "))
while n < 0 :
      print("Error: Número inválido, debe ingresar un valor positivo")
      n=int(input("Numero de telefonos: "))

marca=int(input("Digite el Código correspondiente a la marca: "))
while (marca > 3 and marca < 0):
    print("Error en el codigo de la marca")
    marca=int(input("Digite el código correspondiente a la marca: "))
        
        
plan=int(input("Digite el número correspondiente al plan:"))
if (marca==1 and plan==2):
    z=z+1
elif(marca==2 and plan==1):
    w=w+1
    y=y+1*100/n


print("La cantidad de teléfonos vendidos de marca Sony con plan postpago son: ",)
print("La cantidad de teléfonos vendidos de marca Samsung con plan prepago son: ",)
print("El porcentaje de teléfonos vendidos en prepago es: %",)





                   
                   


























                   
      
      
