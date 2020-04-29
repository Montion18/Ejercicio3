class camion:
    __ident= ''
    __nombrec= ''
    __patente= ''
    __marca= ''
    __tara= ''

    def __init__(self,id=0,nom='',patente='',marca='',tara=0.0):
        self.__ident=id
        self.__nombrec=nom
        self.__patente=patente
        self.__marca=marca
        self.__tara=tara
    def retornatara(self):
        return self.__tara
    def getpatente(self):
        return self.__patente
    def getcond(self):
        return self.__nombrec

   
            


