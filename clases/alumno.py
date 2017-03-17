class Alumno(object):
    nombre = ""
    apellido = ""
    fecha_Nac = ""
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
        ahora = self.lista_Notas[0]
        menor = ahora
        for ahora in self.lista_Notas:
            if ahora < menor:
                menor = ahora
        return menor

    def mayorNota(self):
        ahora = self.lista_Notas[0]
        mayor = ahora
        for ahora in self.lista_Notas:
            if ahora > mayor:
                mayor = ahora
        return mayor

    def promedioNota(self):
        total = 0
        cantidad = 0
        for ahora in self.lista_Notas:
            total = total + ahora
            cantidad = cantidad+1
        return (total/cantidad)