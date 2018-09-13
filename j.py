def funcion1( i ):
    s = ""
    j = 0
    while( i > 4 ):
        s = s + str(i) + " "
        j = 1
        while( j < i ):
            if( j % 3 == 0):
                s = s + str(j) + " "
            j = j + 1
        i = i - 2
    print ("valor de s: ",s)
