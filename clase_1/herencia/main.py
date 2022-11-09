class Pajaro:
    def __init__(self):
        print("Pajaro Listo")

    def whoisthis(self):
        print("Pajaro")

    def swim(self):
        print("Nada rapido")


class Pinguino(Pajaro):
    
    def __init__(self):
        super().__init__()
        print("Pinguino listo")
    def whoisthis(self):
        return super().whoisthis()
    def run(self):
        print("Corre rapido")

timy = Pinguino()
timy.whoisthis()
timy.run()

