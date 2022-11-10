class Ninja:
    def __init__(self, nombre, salud):
        self.nombre=nombre
        self.salud=salud
        self.velocidad=3
        self.fuerza=3
    
    def sayName(self):
        return f"Nombre: {self.nombre}"

    def showStats(self):
        return f"""
                    Nombre: {self.nombre}
                    Fuerza: {self.fuerza}
                    Velocidad: {self.velocidad}
                    Salud: {self.salud}
                """
    def drinkCuzquena(self):
        self.fuerza= self.fuerza + 10
        return f"Fuerza Actual: {self.fuerza}"

obj_ninja = Ninja("Jhomar", 200)

print(obj_ninja.sayName())
print(obj_ninja.drinkCuzquena())

