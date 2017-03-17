from datetime import date

class Materia(object):
    nombre = ""
    lista_Notas = []

class Alumno(object):
    nombre = ""
    apellido = ""
    fecha_Nac = date
    lista_Notas = []
    misMaterias = []

    def setNombre(self,n):
        self.nombre = str(n)

    def setApellido(self,a):
        self.apellido = str(a)

    def setFecha_Nac(self,fn):
        self.fecha_Nac = str(fn)

    def menorNota(self):
        for item in self.misMaterias:
            self.lista_Notas.append(sum(self.misMaterias[item].lista_Notas)/len(self.misMaterias[item].lista_Notas))
        return min(self.lista_Notas)

    def mayorNota(self):
        for item in self.misMaterias:
            self.lista_Notas.append(sum(self.misMaterias[item].lista_Notas)/len(self.misMaterias[item].lista_Notas))
        return max(self.lista_Notas)

    def promedioNotaMateria(self,Nmateria):
        return sum(self.misMaterias[Nmateria].lista_Notas)/len(self.misMaterias[Nmateria].lista_Notas)

    def promedioNotaAlumno(self):
        total = 0
        for item in self.misMaterias:
            total = total + sum(self.misMaterias[item].lista_Notas)
        return total/len(self.misMaterias)

    def agregarMateria(self,nb):
        self.misMaterias.append(Materia)
        self.misMaterias[(len(self.misMaterias))-1].nombre = str(nb)

    def agregarNota(self,nota,Nmateria):
        self.misMaterias[Nmateria].lista_Notas.append(nota)
        print(self.misMaterias[Nmateria].lista_Notas[0])