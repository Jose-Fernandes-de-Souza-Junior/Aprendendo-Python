class Atleta:
    def _init_ (self,aposentado,peso):
        self.aposentado = aposentado
        self.peso = peso

    def aposentar(self):
        print(f"Estou aposentado!{self.aposentado}")

    def aquecer(self):
        print ("Estou aquecido!")

class Corredor(Atleta):
    def __init__(self,aposentado,peso):
        super().__init__(aposentado,peso)

    def correr(self):
        print ("Estou correndo!")

class Nadador(Atleta):
    def _init_(self,aposentado,peso):
        super().__init__(aposentado,peso)

    def nadar (self):
        print ("Estou nadando!")

class Ciclista (Atleta):
    def _init_(self,aposentado,peso):
        super().__init__(aposentado,peso)

    def pedalar (self):
        print ("Estou pedalando!")

class Triatleta (Corredor, Nadador,Ciclista):
    def __init__(self,aposentado,peso):
        super().__init__(aposentado,peso)



competidor = Triatleta (True,10)
competidor.aposentar()
competidor.aquecer()
competidor.correr()
competidor.nadar()
competidor.pedalar()

    

    