class Pajaro: # Clase Padre
    def __init__(self):
        print("Pajaro Listo")

    def whoisthis(self):
        print("Pajaro")

    def swim(self):
        print("Nada rapido")

class Pinguino(Pajaro): # Clase hija
    def __init__(self):
        # Para heredar todo el constructor usamos: 
        super().__init__()
        print("Pinguino listo")
    def whoisthis(self):
        # Para heredar un método usamos:
        return super().whoisthis()
    def run(self):
        print("Corre rapido")

# Creamos una instancia de la clase Pinguino
francis = Pinguino()
francis.whoisthis()
francis.run()

