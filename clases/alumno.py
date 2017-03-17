from datetime import date

class Alumno(object):
    nombre = ""
    apellido = ""
    fecha_Nac = date
    lista_Notas = []

    def setNombre(self,n):
        self.nombre = str(n)

    def setApellido(self,a):
        self.apellido = str(a)

    def setFecha_Nac(self,fn):
        self.fecha_Nac = str(fn)

    def agregarNota(self,nota):
        self.lista_Notas.append(nota)

    def menorNota(self):
        return min(self.lista_Notas)

    def mayorNota(self):
        return max(self.lista_Notas)

    def promedioNota(self):
        return sum(self.lista_Notas)/len(self.lista_Notas)