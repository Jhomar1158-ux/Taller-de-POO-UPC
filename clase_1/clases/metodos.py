class User:
    def __init__(self,nombre, dni, edad, usaLentes):
        #Atributos o caracteristicas
        self.nombre= nombre
        self.dni = dni
        self.edad = edad
        self.usaLentes = usaLentes 
    #Métodos
    def info(self):
        return "Hola Mundo {}".format(self.nombre)
        return "Hola Mundo"
        return f"Nombre: {self.nombre} - DNI: {self.dni} - Edad: {self.edad}"

    def crearLinkGoogleMeet(self):
        pass
    def prenderCamara(self):
        pass
    #...


#### Creamos un objeto dinámico de la clase "User"
obj_rafael = User("Rafael :D", "74357873", 20, False)
# print(obj_rafael.usaLentes)

#Llamando a un método
print(obj_rafael.info())
