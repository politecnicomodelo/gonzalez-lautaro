from clases.mascota import Mascota
from clases.alumno import Alumno


miMascota = Mascota()
miMascota.setNombre("sasha")
miMascota.setTipo(" perro")
print(miMascota.quienSoy())
miAlumno = Alumno()
miAlumno.agregarNota(4)
miAlumno.agregarNota(5)
print(miAlumno.promedioNota())
print(miAlumno.mayorNota())
print(miAlumno.menorNota())