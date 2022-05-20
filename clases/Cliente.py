class Cliente():

    def __init__(self):
        self.__nombre = None
        self.__apellido = None
        self.__cedula = None
        self.__ciudad = None
        self.__nroCuenta = None
        self.__saldo = None

    @property
    def nombre(self):
        return(self.__nombre)

    @property
    def apellido(self):
        return(self.__apellido)

    @property
    def cedula(self):
        return(self.__cedula)

    @property
    def ciudad(self):
        return(self.__ciudad)

    @property
    def nroCuenta(self):
        return(self.__nroCuenta)

    @property
    def saldo(self):
        return(self.__saldo)

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @apellido.setter
    def apellido(self,apellido):
        self.__apellido = apellido

    @cedula.setter
    def cedula(self,cedula):
        if(cedula < 0):
            print("No se puede digitar una cedula negativa")
        else:
            self.__cedula = cedula
    
    @ciudad.setter
    def ciudad(self,ciudad):
        self.__ciudad = ciudad

    @nroCuenta.setter
    def nroCuenta(self,nroCuenta):
        self.__nroCuenta = nroCuenta

    @saldo.setter
    def saldo(self,saldo):
        self.__saldo = saldo
