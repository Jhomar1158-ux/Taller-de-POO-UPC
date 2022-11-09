class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print(f"Precio de venta {self.__maxprice}")
    
    def setMaxPrice(self, price):
        self.__maxprice = price 
    
    def __hola(self):
        print("Hola!")

if __name__=="__main__":
    c = Computer()

    c.sell()

    #Cambiamos el precio máximo
    c.__maxprice=1000
    c.sell()

    #Seteando para cambiar el precio
    c.setMaxPrice(1000)
    c.sell()
