'''
Crea una clase que sea CuentaBancaria.
Tiene atr titular y cantidad
El titular es obligatorio crearlo pero la cantidad no
Un constructor puede estar vacio los datos
getter y setter de manera privada
el metodo __str__ print cuenta y salga info
2 metodos: ingresar y retirar dinero( le paso como atr cantidad )
La cuenta al retirar no puede estar en numeros rojos
GITHUB y pasarlo a Alfonso
'''

class CuentaBancaria:
    def __init__(self, titular, cantidad = 0):
        self.__titular=titular
        self.__cantidad = cantidad
    
    def __str__ (self):
        return self.titular + " la cantidad es --> "+ str(self.cantidad)
    
    def ingresar (self, cantidad):
        if cantidad>0:
            self.__cantidad+= cantidad
            print (f"Se han ingresado {cantidad} euros. Nuevo saldo: {self.__cantidad} euros")
        else:
            print ("La cantidad debe ser mayor que cero")

    def retirar (self, cantidad):
        if cantidad > 0 and cantidad <= self.__cantidad:
            self.__cantidad -= cantidad
            print(f"Se han retirado {cantidad} euros. Nuevo saldo: {self.__cantidad} euros")
        elif cantidad <= 0:
            print("La cantidad a retirar debe ser mayor que cero.")
        else:
            print("Fondos insuficientes.")
        


    @property 
    def titular (self):
        return self.__titular
       
    
    @titular.setter
    def titular (self, nombre):
        self.__titular = nombre

    @property 
    def cantidad (self):
        return self.__cantidad
       
    
    @titular.setter
    def titular (self, valor):
        self.__cantidad = valor
    


c = CuentaBancaria('Daniel', cantidad=1000)
c.ingresar(500)
c.retirar(200)