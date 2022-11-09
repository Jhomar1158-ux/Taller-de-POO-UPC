class User:
    def __init__(self,nombre, dni, edad, usaLentes):
        #Atributos o caracteristicas
        self.nombre= nombre
        self.dni = dni
        self.edad = edad
        self.usaLentes = usaLentes 

#### Creamos un objeto de la clase "User"
# obj_jhomar = User()
# print(obj_jhomar.nombre) #Jhomarcito

#### Creamos un objeto dinámico de la clase "User"
obj_rafael = User("Rafael :D", "74357873", 20, False)
print(obj_rafael.usaLentes)
