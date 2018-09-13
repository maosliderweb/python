N=int(input("cantidad de nums mani: "))
x=int(input("que numero le busco mani: "))
lista=[None]*N
posiciones=[]
cont=0

for i in range(0,N):
    num=int(input("colabore con la lista"))
    lista[i]=num
    if (lista[i]==x):
        cont+=1
        posiciones.append(i)
        
        
print("hay estos numero: ",cont)
print("posiciones:", posiciones)


