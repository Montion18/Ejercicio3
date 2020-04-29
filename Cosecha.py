import csv
from ManejadorC import manejadorc
class Cosecha:
    __lista=[]
    def __init__(self):
        for i in range (20):
            self.__lista.append([])
            for j in range (45):
                self.__lista[i].append(0)
        
        
    def Crearlista(self,m):
        archi=open('Cosechas.csv')
        reader=csv.reader(archi,delimiter=',')
        
        for fila in reader:
            tara=m.tara(int(fila[0])-1)
            peso_real=int(fila[2])-tara
            self.__lista[int(fila[0])-1][int(fila[1])-1]=peso_real
    
    def peso(self,i):
        total=0
        for col in range(45):
            total+=int(self.__lista[i][col])
        return(total)

    def mostrar(self):
        for filas in self.__listab:
            for col in self.__listab:
                print(self.__listab[filas][col])

    def listado(self,dia,m):
        print("PATENTE      CONDUCTOR     CANT.KILOS")
        for i in range(20):
            print(m.patente(i).ljust(2," "),m.conductor(i).center(20," "),self.__lista[i][dia-1])

