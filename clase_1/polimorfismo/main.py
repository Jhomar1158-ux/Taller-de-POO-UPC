
class Loro:

    def volar(self):
        print("Loro volando!")

    def nadar(self):
        print("El loro no puede volar")

class Pinguino:

    def volar(self):
        print("El pinguino no puede volar!")

    def nadar(self):
        print("El pinguino puede nadar")

# Creamos una interfaz común (intermediario)
def volar_test(pajaro):
    pajaro.volar()

#Creamos nuestras instacias

blue = Loro()
timy = Pinguino()

volar_test(blue)
volar_test(timy)
