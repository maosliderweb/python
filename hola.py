filas=3
columnas=3

elmatriz=[[0 for columnas in range (columnas)]for filas in range(filas)]
mensaje="los valores ingresados fueron:\n"
for f in range(0, filas):
    for c in range(0,columnas):
        numero= float(input("de un pinche numerito para ["+str(f)+","+str(c)+"]:"))
        elmatriz[f][c]=numero
        mensaje=mensaje + str(elmatriz[f][c])+"\t"
    mensaje=mensaje+"\n"




lmatriz=[[0 for columnas in range (columnas)]for filas in range(filas)]
mensaj="los valores ingresados fueron:\n"
for f in range(0, filas):
    for c in range(0,columnas):
        numer= float(input("de un pinche numerito para ["+str(f)+","+str(c)+"]:"))
        lmatriz[f][c]=numer
        mensaj=mensaj + str(elmatriz[f][c])+"\t"
    mensaj=mensaj+"\n"

lamatriz=[[0 for columnas in range(columnas)]for filas in range(filas)]

for i in range(columnas):
    for j in range(filas):
        lamatriz[f][c]=elmatriz[f][c]+lmatriz[f][c]

print("resultado")
print(lamatriz)
