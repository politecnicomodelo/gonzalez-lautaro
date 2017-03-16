class Mascota(object):
    nombre = ""
    tipo = ""

    def setNombre (self,n):
        self.nombre = n

    def setTipo (self,t):
        self.tipo = t

    def quienSoy(self):
        return "soy " + self.nombre + " un " + self.tipo