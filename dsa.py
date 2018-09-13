###


def factorialAcumulador(n):
    fac=1  
    for i in range(1,n+1,1):
        fac = fac * i
    print("El factorial de"+str(n)+" es:"+str(fac))



factorialAcumulador(1)
factorialAcumulador(2)
factorialAcumulador(3)
factorialAcumulador(4)
