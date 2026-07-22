class Poleron:
    #metodo constructor
    #funcion que inicializa el objeto que se va a crear 
    #aca se agregan los atributos
    def __init__(self, color, material, modelo):
        self.color = color
        self.material = material
        self.modelo = modelo
        self.uso = False
        print(f"Se ha creado un poleron {self.color} de {self.material} de tipo {self.modelo}")
    def usar(self):
        self.uso = True
        print(f" el poleron {self.color} esta siendo usado")

    def teñir(self, nuevo_color):
        print(f"el poleron {self.color} se tiñio de {nuevo_color}")
        self.color = nuevo_color

poleron1 = Poleron("Naranjo", "Algodon", "Con cierre")
poleron2 = Poleron("Gris", "Poliester", "Canguro")

print(poleron1.material)