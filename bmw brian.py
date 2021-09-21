class carro():
    def __init__(self,name):
        self.nombre = name
    def acelerar (self):
        print("estoy en marcha",self.nombre)
    def frenar (self):
        print("estoy frenando", self.nombre)
    def derrapar(self):
        print("comienzo a derrapar",self.nombre)

bmw010 = carro ("andres")
bmxM3 = carro("brayan")

bmx010.frenar()
bmxM3.acelerar()