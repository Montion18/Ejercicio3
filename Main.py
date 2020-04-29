from Camion import camion
from Cosecha import Cosecha
from ManejadorC import manejadorc

def op0():
    print("salir")

def op1():
    i=int(input("Ingrese el numero del camion: \n"))
    peso=cosecha.peso(i-1)
    print("La cantidad de kilos descargados para el camion {} es: {}".format(i,peso))

def op2():
    i=int(input("Ingrese un dia \n"))
    cosecha.listado(i,m)

switcher= {
    0:op0,
    1:op1,
    2:op2
    
         
    }
def switch(op):
    func = switcher.get(op, lambda: print("Opción incorrecta"))
    func()

if __name__ == '__main__':
    m=manejadorc()
    m.crearcamion()
    cosecha=Cosecha()
    cosecha.Crearlista(m)
    bandera=False
    while not bandera:
        print("---------------MENU-------------")
        print("1.Mostrar la cantidad de kilos para un camion. \n")
        print("2.Mostrar listado. \n")

        op=int(input("Seleccione una opcion.\n"))
        switch(op)
        bandera=int(op)==0


    

   
   