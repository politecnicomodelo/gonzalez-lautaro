from datetime import date

class Jugador(object):
    nombre = ""
    fechaNacimiento = date
    nroCamiseta = 0

    def setNombre(self,n):
        self.nombre = str(n)

    def setFecha_nac(self,f):
        self.fechaNacimiento = f

    def setNroCam(self,n):
        self.nroCamiseta = n