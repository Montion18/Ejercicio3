from Camion import camion
import csv
class manejadorc:
    __lista=[]

    def crearcamion(self):
        
        archivo=open("camiones.csv")
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            cam=camion(fila[0],fila[1],fila[2],fila[3],fila[4])
            self.__lista.append(cam)
        return self.__lista
    def tara(self,id):
        return int(self.__lista[id].retornatara())
    def patente(self,i):
        return self.__lista[i].getpatente()
    def conductor(self,i):
        return self.__lista[i].getcond()