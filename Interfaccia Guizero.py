from guizero import *
import string
import numpy as np
import matplotlib.pyplot as plt



def esplora_file():
    global esplorafile
    esplorafile=app.select_file(filetypes=[["Text documents", "*.txt"]])

def crea_grafico():
    f = open(esplorafile, 'r')
  
    coordX = []
    coordY = []

   

    for riga in f:
        valori = str(riga)  
        Nval = len(valori)          
        valori = valori.strip('\n') 
        valori = valori.split(',')  
        valori = list(valori)       
        print(valori)
        coordX.append(int(valori[0])) 
        coordY.append(int(valori[1])) 

    f.close()  

    print ("X: ",coordX)
    print ("Y: ",coordY)

    coordX.sort()
    coordY.sort()

    print("liste ordinate:") 
    print ("X: ",coordX)
    print ("Y: ",coordY)

    print(type(coordX))
    print(type(coordY))


    plt.scatter(coordX,coordY)
    plt.ylabel('some numbers')
    plt.show()

app = App(title='Interfaccia Grafica')
text = Text(app, text='Genera Grafico', font='Arial', size=16)
push = PushButton(app, text='Scegli il file', command=esplora_file)
push1 = PushButton(app, text='Genera il grafico', command=crea_grafico)



app.display()
